from fastapi import FastAPI
from routers import journalists, articles, auth_users
from fastapi.staticfiles import StaticFiles

app=FastAPI()

app.include_router(journalists.router)
app.include_router(articles.router)
app.include_router(auth_users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def inicio():
    return {"Hola": "World"}