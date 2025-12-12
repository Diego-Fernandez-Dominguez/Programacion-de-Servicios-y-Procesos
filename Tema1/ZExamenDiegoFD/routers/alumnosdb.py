from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import auth_user
from db.models.alumnos import Alumno
from db.client import db_client
from db.schemas.alumno import alumno_schema, alumnos_schema

from bson import ObjectId

router = APIRouter(prefix="/alumnosdb",
                    tags=["alumnosdb"])
    
lista_alumnos = []

@router.get("/", response_model=list[Alumno])
async def users():
    return alumnos_schema(db_client.examen.alumnos.find())

@router.get("", response_model=Alumno)
async def colegio(id: str):
    return search_colegio_id(id)


@router.get("/{id}", response_model=Alumno)
async def colegio(id: str):
    return search_colegio_id(id)


@router.post("/", response_model=Alumno, status_code=201)
async def add_colegio(alumno: Alumno):

    if type(search_alumno(alumno.nombre, alumno.apellidos)) == Alumno:
        raise HTTPException(status_code=400, detail="Alumno already exists")
    
    alumno_dict = alumno.model_dump()
    del alumno_dict["id"]
    
    id= db_client.examen.alumnos.insert_one(alumno_dict).inserted_id

    alumno_dict["id"] = str(id)

    return Alumno(**alumno_dict)
    
@router.put("/{id}", response_model=Alumno)
async def modify_user(id: str, new_alumno: Alumno):

    alumno_dict = new_alumno.model_dump()

    del alumno_dict["id"]   
    try:
        
        db_client.examen.alumnos.find_one_and_replace({"_id":ObjectId(id)}, alumno_dict)
        
        return search_colegio_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Colegio not found")
    

@router.delete("/{id}", response_model=Alumno)
async def delete_user(id:str):
    found = db_client.examen.alumnos.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Colegio not found")
    return Alumno(**alumno_schema(found))
   
def search_colegio_id(id: str):    
    try:
            
        alumno = alumno_schema(db_client.examen.alumnos.find_one({"_id":ObjectId(id)}))
         
        return Alumno(**alumno)
    except:
        return {"error": "Alumno not found"}

def search_alumno(id:str):
    try:
        alumno = alumno_schema(db_client.examen.alumnos.find_one({"id":id}))
        return Alumno(**alumno)
    except:
        return {"error": "Colegio not found"}


def next_id():
    # Calculamos el usuario con el id más alto 
    # y le sumamos 1 a su id
    return (max(alumno.id for alumno in lista_alumnos))+1