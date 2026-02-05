from sqlalchemy import Column, Integer, Float, String
from app.db.base import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    eGFR = Column(Float)
    conditions = Column(String)
