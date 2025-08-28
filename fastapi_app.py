# app.py
from typing import List
import numpy as np
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, conint, confloat

# --------- 1) Schemas (Pydantic) ---------
class PredictIn(BaseModel):
    building_id: str = Field(..., min_length=1)
    airtemperature: confloat(ge=-100, le=100)
    dewtemperature: confloat(ge=-100, le=100)
    windspeed: confloat(ge=0)
    cloudcoverage: confloat(ge=0, le=1)
    precipdepth1hr: confloat(ge=0)
    sealvlpressure: confloat(ge=500, le=1200)
    yearbuilt: conint(ge=1800, le=2100)
    # simple lag features
    energy_per_sqft_lag1: confloat(ge=0)
    energy_per_sqft_lag2: confloat(ge=0)
    energy_per_sqft_lag3: confloat(ge=0)

class PredictOut(BaseModel):
    building_id: str
    predicted_energy_per_sqft: float
    unit: str = "kWh/sqft"

# --------- 2) App ---------
app = FastAPI(title="Energy Forecast API", version="1.0.0")

# load once at startup (replace with your real path)
MODEL = None
FEATURES_IN_ORDER: List[str] = [
    "airtemperature","dewtemperature","windspeed","cloudcoverage",
    "precipdepth1hr","sealvlpressure","yearbuilt",
    "energy_per_sqft_lag1","energy_per_sqft_lag2","energy_per_sqft_lag3",
]

@app.on_event("startup")
def load_model():
    global MODEL
    try:
        MODEL = joblib.load("artifacts/model.pkl")  # e.g., XGBRegressor or RandomForestRegressor
    except Exception as e:
        # keep None so health shows not ready; predict will return 503
        MODEL = None

# --------- 3) Health ---------
@app.get("/healthz")
def health():
    return {"status": "ok" if MODEL is not None else "not_ready"}

# --------- 4) Predict ---------
@app.post("/predict", response_model=PredictOut)
def predict(payload: PredictIn):
    if MODEL is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    # build feature row in the same order as training
    feats = [
        payload.airtemperature, payload.dewtemperature, payload.windspeed, payload.cloudcoverage,
        payload.precipdepth1hr, payload.sealvlpressure, float(payload.yearbuilt),
        payload.energy_per_sqft_lag1, payload.energy_per_sqft_lag2, payload.energy_per_sqft_lag3,
    ]
    X = np.array(feats, dtype=float).reshape(1, -1)
    try:
        y = MODEL.predict(X)  # shape (1,)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")
    return PredictOut(
        building_id=payload.building_id,
        predicted_energy_per_sqft=float(np.round(y[0], 6)),
    )
