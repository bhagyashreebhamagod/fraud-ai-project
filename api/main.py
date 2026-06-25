from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("model/model.pkl")

class Transaction(BaseModel):
    user_id: int
    amount: float
    hour: int
    location_match: int
    is_night: int
    user_avg_amount: float
    amount_diff: float
    high_amount: int

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.post("/predict")
def predict(data: Transaction):

    features = np.array([[
        data.user_id,
        data.amount,
        data.hour,
        data.location_match,
        data.is_night,
        data.user_avg_amount,
        data.amount_diff,
        data.high_amount
    ]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return {
        "fraud": int(prediction),
        "probability": float(probability)
    }
