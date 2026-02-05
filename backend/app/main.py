from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

import app.models  

from app.api import auth, patient, trial, eligibility
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="Clinical Trial Eligibility Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later you can restrict to Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(patient.router, prefix="/patient")
app.include_router(trial.router, prefix="/trial")
app.include_router(eligibility.router, prefix="/eligibility")

@app.get("/")
def health():
    return {"status": "Backend running"}
