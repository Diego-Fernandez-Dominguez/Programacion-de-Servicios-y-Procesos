from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

router=APIRouter(prefix="/programmers", tags=["programmers"])

class Programmer(BaseModel):
    id:int
    DNI:str
    name:str
    surname:str
    telephone:int
    email:str

programmer_list = [
    Programmer(id=1, DNI="12345678A", name="Carlos", surname="García López", telephone=600123456, email="carlos.garcia@example.com"),
    Programmer(id=2, DNI="23456789B", name="María", surname="Fernández Ruiz", telephone=611234567, email="maria.fernandez@example.com"),
    Programmer(id=3, DNI="34567890C", name="Javier", surname="Martín Pérez", telephone=622345678, email="javier.martin@example.com"),
    Programmer(id=4, DNI="45678901D", name="Lucía", surname="Santos Díaz", telephone=633456789, email="lucia.santos@example.com"),
    Programmer(id=5, DNI="56789012E", name="Andrés", surname="Ramírez Gómez", telephone=644567890, email="andres.ramirez@example.com")
]

@router.get("/")
def get_programmers():
    return programmer_list

@router.get("/{id}")
def get_programmer(id:int):
    programmers= [programmer for programmer in programmer_list if programmer.id==id]

    if not programmers:
        raise HTTPException(status_code=404, detail="Programmer no found")
    else:
        return programmers[0]
    
@router.get("")
def get_programmers_by_query(id:int):
    return search_programmers

@router.post("/", status_code=201, response_model=Programmer)
def add_programmer(programmer: Programmer):
    programmer.id=next_id()
    programmer_list.append(programmer)
    return programmer

@router.put("/{id}")
def modify_programmer(id:int, programmer:Programmer):
    for index, saved_programmer in enumerate(programmer_list):
        if saved_programmer.id==id:
            programmer.id=id
            programmer_list[index]=programmer
            return programmer
    raise HTTPException(status_code=404, detail="Programmer not found")

@router.delete("/{id}")
def delete_programmer(id:int):
    for index, saved_programmer in enumerate(programmer_list):
        if saved_programmer.id==id:
            programmer_list.remove(saved_programmer)
            return{}
    raise HTTPException(status_code=404, detail="Programmer not found")


#Functions

def search_programmers(id:int):
    programmers= [programmer for programmer in programmer_list if programmer.id==id]

    if len(programmers) !=0:
        return programmers[0]
    else:
        raise HTTPException(status_code=404, detail="Programmer no found")
        
    
def next_id():
    if not programmer_list:
        return 1
    return max(programmer_list, key=lambda p:p.id).id + 1