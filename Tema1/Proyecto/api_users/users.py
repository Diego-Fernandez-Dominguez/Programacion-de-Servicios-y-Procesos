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

@app.get("/users/")
def get_user(id:int):
    return search_user(id)

@app.post("/users", status_code=201, response_model=User)
def add_user(user:User):

    #Llamamos a la funcion para calcular cual es la id correcta del usuario
    user.id=next_id()

    # Añadimos el usuario a la lista
    user_list.append(user)

    #Pos el return
    return user


@app.put("/users/{id}", response_model=User)
def modify_user(id:int, user:User):

    #El metodo enumerate devuelve el indice de la lista
    #y el usuario almacenado en esa posicion
    for index, saved_user in enumerate (user_list):
        if saved_user.id==id:
            user.id=id
            user_list[index]=user
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{id}")
def delete_user(id:int):
    for saved_user in user_list:
        if saved_user.id==id:
            user_list.remove(saved_user)
            return {"message":"User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

#----------------------

def next_id():
    #Obtenemos el maximo id de la lista de usuarios y le sumamos 1
    return (max(user_list, key=id).id+1)

def search_user(id:int):
    #Metemos en una lista los usuarios que coinciden con la id pasada por parametro
    users=[user for user in user_list if user.id==id]

    #Si la lista esta vacia, lanzamos una excepcion
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    
    #Devolvemos el usuario con la id indicada
    return users[0]
