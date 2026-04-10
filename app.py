from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("models/model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "ML API Running 🚀"}

from pydantic import BaseModel

class InputData(BaseModel):
    age: int
    salary: int
    purchases: int

@app.post("/predict")
def predict(age: int, salary: int, purchases: int):
    data = np.array([[age, salary, purchases]])
    prediction = model.predict(data)

    return {"churn": int(prediction[0])}