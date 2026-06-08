import os
import joblib
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")

ageing_clf = joblib.load(os.path.join(MODELS_DIR, "skill_ageing_classifier.pkl"))
st_model = SentenceTransformer(os.path.join(MODELS_DIR, "sentence_transformer_model"))

def predict_skill_ageing_ml(text):
    emb = st_model.encode([text])
    return ageing_clf.predict(emb)[0]
