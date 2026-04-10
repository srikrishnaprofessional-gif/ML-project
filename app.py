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
def predict(data: InputData):

    input_array = np.array([[data.age, data.salary, data.purchases]])

    prediction = model.predict(input_array)
    prob = model.predict_proba(input_array)

    confidence = max(prob[0])

    return {
        "churn": int(prediction[0]),
        "confidence": float(confidence)
    }
