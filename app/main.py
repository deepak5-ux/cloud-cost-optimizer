# app/main.py

from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import joblib
import os
from dotenv import load_dotenv
from app.model.predictor import predict_instance
from app.model.rule_based import rule_based_fallback

# Load environment variables from .env file
load_dotenv()

# FastAPI app instance
app = FastAPI()

# Security setup: API Key authentication
API_KEY = os.getenv("API_KEY")
api_key_header = APIKeyHeader(name="X-API-Key")

# Load models and encoder (globally for FastAPI)
MODEL_PATH = "models/aws_recommender_model.joblib"
ENCODER_PATH = "models/encoder.joblib"
model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

# Pydantic model for request validation
class WorkloadRequest(BaseModel):
    workload_type: str
    traffic_level: str
    budget: str

    class Config:
        schema_extra = {
            "example": {
                "workload_type": "Web App",
                "traffic_level": "Low",
                "budget": "Low"
            }
        }

# Dependency to validate API key
def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")

# Predict Endpoint
@app.post("/predict/")
async def predict(request: WorkloadRequest, api_key: str = Depends(validate_api_key)):
    """
    Predict the optimal AWS resource instance based on input workload parameters.
    """
    workload_type = request.workload_type
    traffic_level = request.traffic_level
    budget = request.budget

    # First try model prediction
    prediction, error = predict_instance(workload_type, traffic_level, budget)

    # If model fails, fall back to rule-based system
    if error:
        return {"error": "Model prediction failed, using rule-based fallback.", "recommended_instance": rule_based_fallback(workload_type, traffic_level, budget)}
    else:
        return {"recommended_instance": prediction}

# Rule-based fallback Endpoint (optional, can be exposed for transparency)
@app.post("/fallback/")
async def fallback(request: WorkloadRequest, api_key: str = Depends(validate_api_key)):
    """
    Return resource recommendation based on rule-based fallback system.
    """
    recommendation = rule_based_fallback(request.workload_type, request.traffic_level, request.budget)
    return {"recommended_instance": recommendation}
