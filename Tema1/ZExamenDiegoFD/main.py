from fastapi import FastAPI
from routers import colegios, colegiosdb, alumnos, alumnosdb

app = FastAPI()

# Routers
app.include_router(colegios.router)
app.include_router(colegiosdb.router)
app.include_router(alumnos.router)
app.include_router(alumnosdb.router)
#app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"Hello": "World"}