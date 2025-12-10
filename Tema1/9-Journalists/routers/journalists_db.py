from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from db.models.journalists import Journalist
from db.client import db_client
from db.schemas.journalists import journalist_schema, journalists_schema
from bson import ObjectId

router = APIRouter(prefix="/journalistsdb", tags=["journalistsdb"])

journalist_list = []

@router.get("/", response_model=list[Journalist])
async def journalists():
    # El método find() sin parámetros devuelve todos los registros
    # de la base de datos
    return journalists_schema(db_client.journalists_DFD.journalist.find())

@router.get("/{id_journalist}")
def get_journalist(id_journalist: int):
    journalists = [j for j in journalist_list if j.id == id_journalist]
    if not journalists:
        raise HTTPException(status_code=404, detail="Journalist not found")
    return journalists[0]


# Método get tipo query. Sólo busca por id
@router.get("", response_model=Journalist)
async def journalist(id: str):
    return search_journalist_id(id)


@router.post("/", status_code=201, response_model=Journalist)
async def add_journalist(journalist: Journalist):
        #print("dentro de post")
    if type(search_journalist(journalist.name, journalist.surname)) == Journalist:
        raise HTTPException(status_code=409, detail="Journalist already exists")
    
    journalist_dict = journalist.model_dump()
    del journalist_dict["id"]
    # Añadimos el usuario a nuestra base de datos
    # También podemos obtner con inserted_id el id que la base de datos
    # ha generado para nuestro usuario
    id= db_client.journalists_DFD.journalist.insert_one(journalist_dict).inserted_id

    # Añadimos el campo id a nuestro diccionario. Hay que hacerle un cast
    # a string puesto que el id en base de datos se almacena como un objeto,
    # no como un string
    journalist_dict["id"] = str(id)

    # La respuesta de nuestro método es el propio usuario añadido
    # Creamos un objeto de tipo User a partir del diccionario user_dict
    return Journalist(**journalist_dict)
    

@router.put("/{id}", response_model=Journalist)
async def modify_journalist(id: str, new_journalist: Journalist):
    # Convertimos el usuario a un diccionario
    journalist_dict = new_journalist.model_dump()
    # Eliminamos el id en caso de que venga porque no puede cambiar
    del journalist_dict["id"]   
    try:
        # Buscamos el id en la base de datos y le pasamos el diccionario con los datos
        # a modificar del usuario
        db_client.journalists_DFD.journalist.find_one_and_replace({"_id":ObjectId(id)}, journalist_dict)
        # Buscamos el objeto en base de datos y lo retornamos, así comprobamos que efectivamente
        # se ha modificado
        return search_journalist_id(id)    
    except:
        raise HTTPException(status_code=404, detail="Journalist not found")


@router.delete("/{id}", response_model=Journalist)
async def delete_journalist(id:str):
    found = db_client.journalists_DFD.journalist.find_one_and_delete({"_id":ObjectId(id)})

    if not found:
        raise HTTPException(status_code=404, detail="Journalist not found")
    return Journalist(**journalist_schema(found))


# El id de la base de datos es un string, ya no es un entero
def search_journalist_id(id: str):    
    # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
    # así que la controlamos
    try:
        # El id en base de datos no se guarda como un string, sino que es un objeto 
        # Realizamos la conversión    
        journalist = journalist_schema(db_client.journalists_DFD.journalist.find_one({"_id":ObjectId(id)}))
        # Necesitamos convertirlo a un objeto User. 
        return Journalist(**journalist)
    except:
        return {"error": "Journalist not found"}
    

def search_journalist(id: int):
    # La búsqueda me devuelve un objeto del tipo de la base de datos.
    # Necesitamos convertirlo a un objeto User. 
    try:
        # Si algo va mal en la búsqueda dentro de la base de datos se lanzará una excepción,
        # así que la controlamos
        journalist = journalist_schema(db_client.journalists_DFD.journalist.find_one({"id":id}))
        return Journalist(**journalist)
    except:
        return {"error": "Journalist not found"}


def next_id():
    # Calculamos el usuario con el id más alto 
    # y le sumamos 1 a su id
    return (max(journalist.id for journalist in journalist_list))+1
