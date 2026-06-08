from fastapi import FastAPI, UploadFile, File
import shutil
import os

from pydantic import BaseModel


from .utils.analysis import analyze_resume

app = FastAPI(title="Resume ATS Backend")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class AuthRequest(BaseModel):
    email: str
    password: str


@app.get("/")
def home():
    return {"message": "ATS Backend is running 🚀"}







@app.post("/analyze-resume")
async def analyze(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_resume(file_path)

    return result
