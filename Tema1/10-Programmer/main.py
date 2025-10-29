from fastapi import FastAPI
from routers import programmer
from fastapi.staticfiles import StaticFiles

app=FastAPI()

app.include_router(programmer.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def start():
    return{"Wrong":" URL"}