End-to-end Machine Learning project for detecting fraudulent transactions using XGBoost and FastAPI.

## 🚀 Features
- Data generation & preprocessing
- Feature engineering based on user behavior
- ML model training (XGBoost)
- REST API using FastAPI
- Real-time fraud prediction

## 🧠 Tech Stack
Python, Pandas, NumPy, Scikit-learn, XGBoost, FastAPI, Uvicorn

## 📁 Project Structure
fraud_ai_project/
├── data/
├── src/
├── api/
├── model/

## ▶️ How to Run
pip install -r requirements.txt
python3 data/create_data.py
python3 src/train.py
uvicorn api.main:app --reload

## 📌 API Endpoint
POST /predict

Example input:
{
  "features": [5000, 23, 0, 4000, 1000, 0, 1]
}
