from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def xokas():
    return {"Estoy": "codificando", "con un": "microprocesador X264"}