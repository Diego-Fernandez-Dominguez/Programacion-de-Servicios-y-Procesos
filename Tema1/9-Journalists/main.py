from fastapi import FastAPI
from routers import journalists, articles
from fastapi.staticfiles import StaticFiles

app=FastAPI()

app.include_router(journalists.router)
app.include_router(articles.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"Hola": "World"}