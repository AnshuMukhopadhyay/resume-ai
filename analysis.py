import os
import joblib
import numpy as np
import re
from sentence_transformers import SentenceTransformer
from .pdf_utils import extract_text_from_pdf, clean_resume
from .skill_maps import ROLE_SKILLS
from .buzzwords import extract_buzzwords
from .skill_ageing import predict_skill_ageing_ml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

clf = joblib.load(os.path.join(MODELS_DIR, "resume_classifier.pkl"))
st_model = SentenceTransformer(os.path.join(MODELS_DIR, "sentence_transformer_model"))


def predict_resume_from_pdf(pdf_path):
    raw = extract_text_from_pdf(pdf_path)
    if not raw.strip():
        return {"role": None, "confidence": 0.0}

    clean = clean_resume(raw)
    emb = st_model.encode([clean])

    role = clf.predict(emb)[0]
    confidence = float(np.max(clf.predict_proba(emb)[0]))

    return {
        "role": role,
        "confidence": round(confidence * 100, 2)
    }


def calculate_skill_score(resume_text, role):
    skills = ROLE_SKILLS.get(role, {})
    score = 0

    for skill, weight in skills.items():
        if skill.lower() in resume_text.lower():
            score += weight

    return min(score, 100)


def get_best_role_by_max_score(resume_text):
    best_role = None
    best_score = 0
    role_scores = {}

    for role in ROLE_SKILLS:
        score = calculate_skill_score(resume_text, role)
        role_scores[role] = score

        if score > best_score:
            best_score = score
            best_role = role

    return best_role, best_score, role_scores

def analyze_resume(pdf_path, threshold=60):
    # ---- ML PREDICTION (SUPPORTING ONLY) ----
    result = predict_resume_from_pdf(pdf_path)
    ml_confidence = result["confidence"]  # already in %

    raw_text = extract_text_from_pdf(pdf_path)
    resume_text = raw_text.lower()

    # ====================================================
    # 🔥 MAX SCORE ROLE SELECTION (CORE LOGIC)
    # ====================================================
    best_role, skill_score, role_scores = get_best_role_by_max_score(resume_text)

    # ---- FINAL CONFIDENCE (HYBRID) ----
    final_confidence = round(
        0.6 * ml_confidence + 0.4 * skill_score, 2
    )

    # ---- BUZZWORDS ----
    buzzwords = extract_buzzwords(raw_text, best_role)

    # ---- MISSING SKILLS ----
    required_skills = {
        skill.lower()
        for skill in ROLE_SKILLS.get(best_role, {}).keys()
    }

    found_skills = {b.lower() for b in buzzwords}
    missing_skills = [s.title() for s in (required_skills - found_skills)]

    # ---- SKILL AGEING ----
    sentences = re.split(r'[.\n]', raw_text)
    skill_ageing = {}

    for skill in buzzwords:
        relevant = [s for s in sentences if skill.lower() in s.lower()]
        skill_ageing[skill] = (
            predict_skill_ageing_ml(relevant[0]) if relevant else "Unknown"
        )

    # ---- STATUS ----
    if final_confidence >= threshold:
        status = "Strong Profile"
    elif final_confidence >= 40:
        status = "Moderate Match"
    else:
        status = "Needs Improvement"

    return {
        "best_role": best_role,
        "confidence_percent": final_confidence,
        "ml_confidence": ml_confidence,
        "skill_match_score": skill_score,
        "status": status,
        "strengths": buzzwords,
        "missing_skills": missing_skills,
        "skill_ageing": skill_ageing,
        "role_scores": role_scores  # 🔥 recruiter gold
    }


