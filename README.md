# AI Fraud Detection System

## Overview

An end-to-end Machine Learning project that detects fraudulent transactions using XGBoost and serves predictions through a FastAPI REST API.

## Features

* Feature Engineering Pipeline
* Fraud Detection using XGBoost
* REST API with FastAPI
* Dockerized Deployment
* Real-time Prediction Endpoint

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* XGBoost
* FastAPI
* Docker
* Git & GitHub

## Run Locally

```bash
pip install -r requirements.txt
python src/train.py
uvicorn api.main:app --reload
```

## Run with Docker

```bash
docker build -t fraud-ai-app .
docker run -p 8000:8000 fraud-ai-app
```

## API Endpoint

POST /predict

Example Request:

```json
{
  "user_id": 1,
  "amount": 5000,
  "hour": 23,
  "location_match": 1,
  "is_night": 1,
  "user_avg_amount": 3000,
  "amount_diff": 2000,
  "high_amount": 0
}
```
