from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.eligibility import EligibilityResult
from app.services.inclusion import check_age
from app.services.exclusion import check_egfr
from app.services.contradiction import detect_contradiction

router = APIRouter()

# 🔹 Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/analyze")
def analyze_eligibility(
    payload: dict,
    patient_id: int,
    trial_id: int,
    db: Session = Depends(get_db)
):
    """
    payload expected as:
    {
      "patient": {
        "age": int,
        "eGFR": float
      }
    }
    """

    try:
        # 🔹 Extract nested patient object
        if "patient" not in payload:
            raise HTTPException(
                status_code=400,
                detail="Request body must contain 'patient' object"
            )

        patient = payload["patient"]

        if "age" not in patient or "eGFR" not in patient:
            raise HTTPException(
                status_code=400,
                detail="Patient must contain 'age' and 'eGFR'"
            )

        age = int(patient["age"])
        egfr = float(patient["eGFR"])

        # 1️⃣ Inclusion logic
        inclusion = check_age(age)

        # 2️⃣ Exclusion logic
        exclusion = check_egfr(egfr)

        # 3️⃣ Silent exclusion detection
        result = detect_contradiction(inclusion, exclusion, patient)

        # 4️⃣ Final decision
        if result.get("silent_exclusion"):
            final_status = "NOT ELIGIBLE"
            explanation = result["explanation"]
        else:
            final_status = "ELIGIBLE"
            explanation = "Patient meets all eligibility criteria."

        # 5️⃣ Save to database
        record = EligibilityResult(
            patient_id=patient_id,
            trial_id=trial_id,
            status=final_status,
            explanation=explanation
        )

        db.add(record)
        db.commit()
        db.refresh(record)

        # 6️⃣ Response
        return {
            "eligibility_id": record.id,
            "status": final_status,
            "inclusion": inclusion,
            "exclusion": exclusion,
            "explanation": explanation
        }

    except HTTPException:
        raise
    except Exception as e:
        # Any unexpected error will now be visible
        raise HTTPException(status_code=500, detail=str(e))
