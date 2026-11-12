"""TODO: FastAPI prediction endpoint using the saved pipeline."""
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "model" / "claim_model.joblib"
app = FastAPI(title="Claim Outcome Prediction API")

class ClaimRequest(BaseModel):
    payer: str
    provider: str
    cpt_code: str
    diagnosis_code: str
    billed_amount: float = Field(gt=0)
    patient_age: int = Field(ge=0, le=120)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(claim: ClaimRequest):
    # TODO: load saved pipeline, convert request to one-row DataFrame,
    # call predict() and predict_proba(), map probabilities using
    # pipeline.classes_, and return required response shape.
    # Return a clear service error if the model file is unavailable.
    raise HTTPException(status_code=501, detail="Complete /predict before use.")
