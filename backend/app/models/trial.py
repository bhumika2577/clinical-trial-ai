from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Trial(Base):
    __tablename__ = "trials"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    pdf_path = Column(String)
