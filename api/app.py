import mlflow
import pandas as pd

from fastapi import FastAPI
from pydantic import BaseModel


mlflow.set_tracking_uri("sqlite:///mlflow.db")

app = FastAPI(title="Customer Churn Prediction API")


class Customer(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float
    contract_type: str
    internet_service: str
    tech_support: str


model = mlflow.sklearn.load_model(
    "runs:/c7baa9bbad6446d38791795b27bd9616/churn_model"
)


@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}


@app.post("/predict")
def predict(customer: Customer):

    data = pd.DataFrame([customer.model_dump()])

    prediction = model.predict(data)[0]

    return {
        "churn_prediction": int(prediction),
        "churn": "Yes" if prediction == 1 else "No"
    }