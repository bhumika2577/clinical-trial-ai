from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class EligibilityResult(Base):
    __tablename__ = "eligibility_results"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    trial_id = Column(Integer, ForeignKey("trials.id"))
    status = Column(String)
    explanation = Column(String)
