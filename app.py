from http.client import HTTPException
from fastapi import HTTPException
from fastapi import FastAPI

from interfaces import dataTest

app = FastAPI()

cursos = {
    "Programacion":{"Fundamentos":15, "POO":20},
    "Matematicas":{"Especiales":20, "Calculo":25}    
}

@app.get("/")
def index():
    return {"Mensaje":"API Running"}

@app.get("/cursos")
def getCursos():
    return cursos

@app.get("/cursos/{tipo}")
def tipoCursos(tipo:str):
    if tipo not in cursos:
        raise HTTPException(status_code=404, detail = "Tipo de curso no encontrado")
    return{"curso": cursos[tipo]}

@app.post("/asignatura")
def asignatura(data: dataTest):
    data = data.model_dump()
    print(data)
    return {"asignatura recibida":data}

if __name__=="__main__":
    app.run()
