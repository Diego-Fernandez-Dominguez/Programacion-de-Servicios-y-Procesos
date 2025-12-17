from fastapi import FastAPI
from routers import journalists, products, auth_journalists, journalists_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(journalists.router)
app.include_router(products.router)
app.include_router(auth_journalists.router)
app.include_router(journalists_db.router)
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"Hello": "World"}
