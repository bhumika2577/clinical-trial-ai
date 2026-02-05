from fastapi import APIRouter, UploadFile, File
from app.services.pdf_parser import extract_text

router = APIRouter()

@router.post("/upload")
def upload_trial(file: UploadFile = File(...)):
    content = extract_text(file.file)
    return {"message": "Trial uploaded", "length": len(content)}



from app.models.trial import Trial
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import os
import shutil

from app.db.session import SessionLocal
from app.models.trial import Trial
from app.services.pdf_parser import extract_text

router = APIRouter()

# 🔹 Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🔹 Directory to store uploaded PDFs
UPLOAD_DIR = "uploaded_trials"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
def upload_trial(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # 1️⃣ Save PDF to disk
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # 2️⃣ Extract text from PDF (for future RAG use)
    extracted_text = extract_text(file_path)

    # 3️⃣ Save trial metadata to database
    new_trial = Trial(
        title=file.filename,
        pdf_path=file_path
    )

    db.add(new_trial)
    db.commit()
    db.refresh(new_trial)

    return {
        "message": "Trial uploaded and saved to database",
        "trial_id": new_trial.id,
        "pdf_path": file_path,
        "extracted_text_length": len(extracted_text)
    }
