from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import app.models
from app.api import auth, patient, trial, eligibility

app = FastAPI(title="Clinical Trial Eligibility Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",          # local React
        "https://clinical-trial-ai-frontend.vercel.app",  # future Vercel
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(patient.router, prefix="/patient")
app.include_router(trial.router, prefix="/trial")
app.include_router(eligibility.router, prefix="/eligibility")

@app.get("/")
def health():
    return {"status": "Backend running"}
