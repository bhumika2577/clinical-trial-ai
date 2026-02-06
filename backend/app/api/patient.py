from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List

from app.db.session import SessionLocal
from app.models.patient import Patient

router = APIRouter()


# ---------- DB dependency ----------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- Schema ----------
class PatientCreate(BaseModel):
    age: int
    egfr: float
    conditions: List[str]


# ---------- Routes ----------
# @router.post("/")
# def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
#     new_patient = Patient(
#         age=patient.age,
#         eGFR=patient.egfr,
#         conditions=", ".join(patient.conditions)
#     )

#     db.add(new_patient)
#     db.commit()
#     db.refresh(new_patient)

#     return {
#         "message": "Patient saved to database",
#         "patient_id": new_patient.id
#     }


@router.post("/")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    print("🔥 CREATE PATIENT CALLED:", patient)

    new_patient = Patient(
        age=patient.age,
        eGFR=patient.egfr,
        conditions=", ".join(patient.conditions)
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {
        "message": "Patient saved to database",
        "patient_id": new_patient.id
    }


@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()
