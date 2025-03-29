import pickle
from fastapi import FastAPI
import numpy as np

from interfaces import DiabetesData


app = FastAPI()

with open("RFDiabetesv132.pkl","rb") as file:
    model = pickle.load(file)

labels = ["Sano", "Enfermo"]

@app.get("/")
def index():
    return{"Mensaje":"API running"}

@app.post("/predict")
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

   ## return {"prediction":"ok"}

    ##resultado = "Sano" if prediction[0] == 0 else "Enfermo"
    ##print("prediction:", prediction)
    ##return {"prediction": resultado}



if __name__=="__main__":
    app.run()
