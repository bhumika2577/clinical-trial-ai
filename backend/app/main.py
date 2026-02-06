from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.models
from app.db.session import engine
from app.db.base import Base
from app.api import auth, patient, trial, eligibility

app = FastAPI(title="Clinical Trial Eligibility Engine")

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://clinical-trial-ai-frontend.vercel.app",  # optional
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- CREATE TABLES ----------------
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# ---------------- ROUTERS ----------------
app.include_router(auth.router, prefix="/auth")
app.include_router(patient.router, prefix="/patient")
app.include_router(trial.router, prefix="/trial")
app.include_router(eligibility.router, prefix="/eligibility")

@app.get("/")
def health():
    return {"status": "Backend running"}
