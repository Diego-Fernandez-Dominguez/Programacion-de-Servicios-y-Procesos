from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/journalists", tags=["journalists"])

class Journalist(BaseModel):
    id: int
    dni: str
    name: str
    surname: str
    telephone: int
    specialty: str

journalist_list = [
    Journalist(id=1, dni="12345678A", name="Eusebio", surname="Perez", telephone=678912345, specialty="Sports"),
    Journalist(id=2, dni="87654321B", name="Daniel", surname="Lopez", telephone=612345678, specialty="Politics"),
    Journalist(id=3, dni="11223344C", name="Luis", surname="Garcia", telephone=698765432, specialty="Culture"),
]

@router.get("/")
def get_journalists():
    return journalist_list

@router.get("/{id_journalist}")
def get_journalist(id_journalist: int):
    journalists = [j for j in journalist_list if j.id == id_journalist]
    if not journalists:
        raise HTTPException(status_code=404, detail="Journalist not found")
    return journalists[0]

@router.get("/query/")
def get_journalist_by_query(id: int):
    return search_journalist(id)

@router.post("/", status_code=201, response_model=Journalist)
def add_journalist(journalist: Journalist):
    journalist.id = next_id()
    journalist_list.append(journalist)
    return journalist

@router.put("/{id}")
def modify_journalist(id: int, journalist: Journalist):
    for index, saved_journalist in enumerate(journalist_list):
        if saved_journalist.id == id:
            journalist.id = id
            journalist_list[index] = journalist
            return journalist
    raise HTTPException(status_code=404, detail="Journalist not found")

@router.delete("/{id}")
def delete_journalist(id: int):
    for saved_journalist in journalist_list:
        if saved_journalist.id == id:
            journalist_list.remove(saved_journalist)
            return {}
    raise HTTPException(status_code=404, detail="Journalist not found")

def search_journalist(id: int):
    journalists = [j for j in journalist_list if j.id == id]
    if len(journalists) != 0:
        return journalists[0]
    else:
        return {"error": "No journalist found"}

def next_id():
    if not journalist_list:
        return 1
    return max(journalist_list, key=lambda j: j.id).id + 1
