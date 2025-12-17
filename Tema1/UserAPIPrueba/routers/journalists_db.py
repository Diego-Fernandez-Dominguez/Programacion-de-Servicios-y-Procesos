from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import auth_user
from db.models.journalist import Journalist
from db.client import db_client
from db.schemas.journalist import journalist_schema, journalists_schema

from bson import ObjectId

router = APIRouter(prefix="/journalistsdb", tags=["journalistsdb"])

# la siguiente lista pretende simular una base de datos para probar nuestra API
journalists_list = []

@router.get("/", response_model=list[Journalist])
async def journalists():
    # El método find() sin parámetros devuelve todos los registros
    return journalists_schema(db_client.test.journalists.find())

# Método get tipo query. Sólo busca por id
@router.get("", response_model=Journalist)
async def journalist(id: str):
    return search_journalist_id(id)

# Método get por id
@router.get("/{id}", response_model=Journalist)
async def journalist(id: str):
    return search_journalist_id(id)

@router.post("/", response_model=Journalist, status_code=201)
async def add_journalist(journalist: Journalist):
    if type(search_journalist(journalist.name, journalist.surname)) == Journalist:
        raise HTTPException(status_code=409, detail="Journalist already exists")
    
    journalist_dict = journalist.model_dump()
    del journalist_dict["id"]
    id = db_client.test.journalists.insert_one(journalist_dict).inserted_id

    journalist_dict["id"] = str(id)
    return Journalist(**journalist_dict)
    
@router.put("/{id}", response_model=Journalist)
async def modify_journalist(id: str, new_journalist: Journalist):
    journalist_dict = new_journalist.model_dump()
    del journalist_dict["id"]   
    try:
        db_client.test.journalists.find_one_and_replace({"_id":ObjectId(id)}, journalist_dict)
        return search_journalist_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Journalist not found")
    

@router.delete("/{id}", response_model=Journalist)
async def delete_journalist(id:str):
    found = db_client.test.journalists.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Journalist not found")
    return Journalist(**journalist_schema(found))
   
def search_journalist_id(id: str):    
    try:
        journalist = journalist_schema(db_client.test.journalists.find_one({"_id":ObjectId(id)}))
        return Journalist(**journalist)
    except:
        return {"error": "Journalist not found"}

def search_journalist(name: str, surname: str):
    try:
        journalist = journalist_schema(db_client.test.journalists.find_one({"name":name, "surname":surname}))
        return Journalist(**journalist)
    except:
        return {"error": "Journalist not found"}

def next_id():
    return (max(journalist.id for journalist in journalists_list))+1
