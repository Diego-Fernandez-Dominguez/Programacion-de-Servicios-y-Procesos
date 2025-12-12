from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import auth_user
from db.models.colegio import Colegio
from db.client import db_client
from db.schemas.colegio import colegio_schema, colegios_schema

from bson import ObjectId

router = APIRouter(prefix="/colegiosdb",
                    tags=["colegiosdb"])
    
lista_colegios = []

@router.get("/", response_model=list[Colegio])
async def users():
    return colegios_schema(db_client.examen.colegios.find())

@router.get("", response_model=Colegio)
async def colegio(id: str):
    return search_colegio_id(id)


@router.get("/{id}", response_model=Colegio)
async def colegio(id: str):
    return search_colegio_id(id)


@router.post("/", response_model=Colegio, status_code=201)
async def add_colegio(colegio: Colegio):
    
    if colegio.tipo != "publico" or colegio.tipo != "concertado" or colegio.tipo != "privado":
            raise HTTPException(status_code=400, detail="Colegio type is incorrect")

    if type(search_colegio(colegio.nombre)) == Colegio:
        raise HTTPException(status_code=400, detail="Colegio already exists")
    
    colegio_dict = colegio.model_dump()
    del colegio_dict["id"]
    
    id= db_client.examen.colegios.insert_one(colegio_dict).inserted_id

    colegio_dict["id"] = str(id)

    return Colegio(**colegio_dict)
    
@router.put("/{id}", response_model=Colegio)
async def modify_user(id: str, new_colegio: Colegio):

    colegio_dict = new_colegio.model_dump()

    del colegio_dict["id"]   
    try:
        
        db_client.examen.colegios.find_one_and_replace({"_id":ObjectId(id)}, colegio_dict)
        
        return search_colegio_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Colegio not found")
    

@router.delete("/{id}", response_model=Colegio)
async def delete_user(id:str):
    found = db_client.examen.colegios.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Colegio not found")
    return Colegio(**colegio_schema(found))
   
def search_colegio_id(id: str):    
    try:
            
        colegio = colegio_schema(db_client.examen.colegios.find_one({"_id":ObjectId(id)}))
         
        return Colegio(**colegio)
    except:
        return {"error": "Colegio not found"}



def search_colegio(id:str):
    try:
        colegio = colegio_schema(db_client.examen.colegios.find_one({"id":id}))
        return Colegio(**colegio)
    except:
        return {"error": "Colegio not found"}


def next_id():
    return (max(colegio.id for colegio in lista_colegios))+1