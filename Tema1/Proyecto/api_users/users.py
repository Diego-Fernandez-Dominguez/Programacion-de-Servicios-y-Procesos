from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    id: int
    name:str
    surname:str
    age:int

user_list=[User(id=1 ,name="Euseboi", surname="Chef", age=78),
           User(id=2 ,name="Adrian", surname="Diaz", age=19),
           User(id=3 ,name="Dario", surname="Fernandez", age=20)]

@app.get("/users")
def users():
    return user_list

@app.get("/users/{id_user}")
def get_user(id_user:int):
    return search_user(id_user)

@app.get("/users")
def get_user(id:int):
    return search_user(id)

def search_user(id:int):
    users=[user for user in user_list if user.id==id]

    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    
    return users[0]
