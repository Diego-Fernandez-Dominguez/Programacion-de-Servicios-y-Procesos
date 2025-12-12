from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import auth_user

router = APIRouter(prefix="/colegios",
                   tags=["colegios"])

class Colegio(BaseModel):
    id: int
    nombre:str
    distrito:str
    tipo:str
    direccion:str
    
lista_colegios = [Colegio(id="1", nombre = "IES Nervion", distrito = "Nervion", tipo="publico", direccion="Sevilla"),
                  Colegio(id="2", nombre = "San Francisco Solano", distrito = "Triana", tipo="concertado", direccion="Sevilla")]

@router.get("/")
def colegios():
    return lista_colegios


@router.get("/{id}", response_model=Colegio)
def colegio(id: int):
    colegios = search_colegio(id)
    if len(colegios) != 0:
        return colegios[0]
    raise HTTPException(status_code=404, detail="Colegio not found")

@router.get("/{id}", response_model=Colegio)
def colegio(id: int):
    pass

@router.post("/", status_code=201, response_model=Colegio)
def add_colegio(colegio: Colegio, user = Depends(auth_user)):

    if colegio.tipo != "publico" and colegio.tipo != "concertado" and colegio.tipo != "privado":
        raise HTTPException(status_code=400, detail="Colegio type is incorrect") 
    
    colegio.id = next_id()

    lista_colegios.append(colegio)
    return colegio
    
@router.put("/{id}", response_model=Colegio)
def modify_colegio(id: int, colegio: Colegio):
    for index, colegio_guardado in enumerate(lista_colegios):
        if colegio_guardado.id == id:
            colegio.id = id
            lista_colegios[index] = colegio
            return colegio
    
    raise HTTPException(status_code=404, detail="Colegio not found")

@router.delete("/{id}", response_model=Colegio)
def delete_colegio(id:int):
    for colegio_guardado in lista_colegios:
        if colegio_guardado.id == id:
            lista_colegios.remove(colegio_guardado)
            return {}
    raise HTTPException(status_code=404, detail="Colegio not found")
   
def search_colegio(id: int):

    return [colegio for colegio in lista_colegios if colegio.id == id]

def next_id():

    return max([colegio.id for colegio in lista_colegios]) + 1