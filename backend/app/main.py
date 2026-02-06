# from fastapi.middleware.cors import CORSMiddleware

# from fastapi import FastAPI

# import app.models  

# from app.api import auth, patient, trial, eligibility
# from app.db.session import engine
# from app.db.base import Base

# app = FastAPI(title="Clinical Trial Eligibility Engine")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],   # later you can restrict to Vercel URL
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# #Base.metadata.create_all(bind=engine)

# app.include_router(auth.router, prefix="/auth")
# app.include_router(patient.router, prefix="/patient")
# app.include_router(trial.router, prefix="/trial")
# app.include_router(eligibility.router, prefix="/eligibility")

# @app.get("/")
# def health():
#     return {"status": "Backend running"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# IMPORTANT: this ensures all models are registered
import app.models  

from app.api import auth, patient, trial, eligibility
from app.db.base import Base
from app.db.session import engine

app = FastAPI(
    title="Clinical Trial Eligibility Engine",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*"
        # Later replace "*" with:
        # "https://clinical-trial-ai.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(patient.router, prefix="/patient", tags=["Patient"])
app.include_router(trial.router, prefix="/trial", tags=["Trial"])
app.include_router(eligibility.router, prefix="/eligibility", tags=["Eligibility"])

@app.get("/", tags=["Health"])
def health():
    return {"status": "Backend running"}
