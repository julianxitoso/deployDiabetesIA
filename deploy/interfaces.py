from pydantic import BaseModel

class dataTest(BaseModel):
    nombre: str
    estudiantes: float


class DiabetesData(BaseModel):
    Pregnancies: int
    Glucose: float
    Age: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: int
    DiabetesPedigreeFunction:float