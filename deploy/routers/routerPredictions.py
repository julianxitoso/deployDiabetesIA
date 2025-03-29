import pickle
import numpy as np
from fastapi import APIRouter
from interfaces import DiabetesData

router = APIRouter()

with open("RFDiabetesv132.pkl","rb") as file:
    model = pickle.load(file)

labels = ["Enfermo", "Sano"]


@router.post("/predict")
def predict(data: DiabetesData):
    data = data.model_dump()
    print(data)

    Pregnancies=data["Pregnancies"]
    Glucose=data["Glucose"]
    Age=data["Age"]
    BloodPressure=data["BloodPressure"]
    SkinThickness=data["SkinThickness"]
    Insulin=data["Insulin"]
    BMI=data["BMI"]
    DiabetesPedigreeFunction=data["DiabetesPedigreeFunction"]

    xin = np.array([Pregnancies,Glucose,Age,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction]).reshape(1,8)

    prediction = model.predict(xin)

    print("prediction: ", labels[prediction[0]])
    return{"prediction ": labels[prediction[0]]}


