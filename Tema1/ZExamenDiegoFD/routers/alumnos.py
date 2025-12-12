from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from .auth_users import auth_user

router = APIRouter(prefix="/alumnos",
                   tags=["alumnos"])

class Alumno(BaseModel):
    id: int
    nombre:str
    apellidos:str
    fecha_nacimiento:str
    curso:str
    repetidor: bool
    id_colegio:int
    
lista_alumnos = [Alumno(id=1, nombre = "Diego", apellidos="Fernandez Dominguez", fecha_nacimiento="03/07/2006", curso="2BACH", repetidor=False, id_colegio=1),
                 Alumno(id=2, nombre = "Adrian", apellidos="Moreno Montero", fecha_nacimiento="012/04/2006", curso="2ESO", repetidor=True, id_colegio=2)]

@router.get("/")
def alumnos():
    return lista_alumnos


@router.get("/{id}", response_model=Alumno)
def alumno(id: int):
    alumnos = search_alumno(id)
    if len(alumnos) != 0:
        return alumnos[0]
    raise HTTPException(status_code=404, detail="Alumno not found")


@router.get("/{id_colegio}/alumnos", response_model=Alumno)
def alumno(id_colegio: int):
    alumnos = search_alumno(id_colegio)
    if len(alumnos) != 0:
        return alumnos[0]
    raise HTTPException(status_code=404, detail="Alumno not found")

@router.get("/{id}", response_model=Alumno)
def alumno(id: int):
    pass

@router.post("/", status_code=201, response_model=Alumno)
def add_alumno(alumno: Alumno, user = Depends(auth_user)):
    
    alumno.id = next_id()

    lista_alumnos.append(alumno)
    return alumno
    
@router.put("/{id}", response_model=Alumno)
def modify_alumno(id: int, alumno: Alumno):
    for index, alumno_guardado in enumerate(lista_alumnos):
        if alumno_guardado.id == id:
            alumno.id = id
            lista_alumnos[index] = alumno
            return alumno
    
    raise HTTPException(status_code=404, detail="Alumno not found")

@router.delete("/{id}", response_model=Alumno)
def delete_alumno(id:int):
    for alumno_guardado in lista_alumnos:
        if alumno_guardado.id == id:
            lista_alumnos.remove(alumno_guardado)
            return {}
    raise HTTPException(status_code=404, detail="Alumno not found")
   
def search_alumno(id: int):
    return [alumno for alumno in lista_alumnos if alumno.id == id]

def next_id():
    return max([alumno.id for alumno in lista_alumnos]) + 1