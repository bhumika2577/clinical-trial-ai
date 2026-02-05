from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.patient import Patient

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
def upload_patient(patient: dict, db: Session = Depends(get_db)):
    new_patient = Patient(
        age=patient["age"],
        eGFR=float(patient["eGFR"]),
        conditions=", ".join(patient.get("conditions", []))
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {
        "message": "Patient saved to database",
        "patient_id": new_patient.id
    }
