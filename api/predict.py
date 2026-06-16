
import os
import sys
import json
import numpy as np
import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from functools import lru_cache

app = FastAPI(title="Symptom-to-Disease Predictor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@lru_cache(maxsize=1)
def load_artifacts():
    model = joblib.load(os.path.join(BASE, "models", "best_model.pkl"))
    le = joblib.load(os.path.join(BASE, "models", "label_encoder.pkl"))
    features = joblib.load(os.path.join(BASE, "models", "feature_names.pkl"))
    return model, le, features


class PredictRequest(BaseModel):
    symptoms: List[str]


@app.get("/api/metadata")
def get_metadata():
    _, le, features = load_artifacts()
    return {"features": features, "diseases": list(le.classes_)}


@app.post("/api/predict")
def predict(req: PredictRequest):
    if len(req.symptoms) < 2:
        raise HTTPException(status_code=400, detail="Select at least 2 symptoms.")

    model, le, features = load_artifacts()

    vec = {f: 0 for f in features}
    unknown = []
    for sym in req.symptoms:
        key = sym.strip().lower().replace(" ", "_").replace("-", "_")
        if key in vec:
            vec[key] = 1
        else:
            unknown.append(sym)

    X = pd.DataFrame([vec])
    proba = model.predict_proba(X)[0]
    top3_idx = np.argsort(proba)[::-1][:3]

    top3 = [
        {
            "rank": int(i + 1),
            "disease": le.inverse_transform([idx])[0],
            "confidence": round(float(proba[idx]) * 100, 2),
        }
        for i, idx in enumerate(top3_idx)
    ]

    all_probs = sorted(
        [
            {"disease": le.inverse_transform([i])[0], "probability": round(float(p) * 100, 2)}
            for i, p in enumerate(proba)
        ],
        key=lambda x: x["probability"],
        reverse=True,
    )

    return {"top3": top3, "all_probabilities": all_probs, "unknown_symptoms": unknown}
