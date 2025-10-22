from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class Journalist(BaseModel):
    id: int
    dni:str
    name:str
    surname:str
    telephone:int
    specialty:str
    

journalist_list=[Journalist(id=1 ,dni="12345678A", name="Euseboi", surname="Perez", telephone=678912345, specialty="Sports"),
           Journalist(id=2 ,dni="87654321B", name="Daniel", surname="Lopez", telephone=612345678, specialty="Politics"),
           Journalist(id=3 ,dni="11223344C", name="Luis", surname="Garcia", telephone=698765432, specialty="Culture"),
           Journalist(id=4 ,dni="44332211D", name="Ana", surname="Martinez", telephone=600112233, specialty="Technology"),
           Journalist(id=5 ,dni="55667788E", name="Marta", surname="Sanchez", telephone=699887766, specialty="Health")]


# Get all journalists
@app.get("/journalists")
def journalists():
    return journalist_list

@app.get("/journalists/")
def get_journalists():
    return journalist_list

# Id
@app.get("/journalists/{id_journalist}")
def get_journalist(id_journalist:int):
    return search_journalist(id_journalist)


@app.post("/journalists", status_code=201, response_model=Journalist)
def add_journalist(journalist:Journalist):

    journalist.id=next_id()
    journalist_list.append(journalist)
    return journalist


@app.put("/journalists/{id}", response_model=Journalist)
def modify_journalist(id:int, journalist:Journalist):

    for index, saved_journalist in enumerate (journalist_list):
        if saved_journalist.id==id:
            journalist.id=id
            journalist_list[index]=journalist
            return journalist
    raise HTTPException(status_code=404, detail="Journalist not found")


@app.delete("/journalists/{id}")
def delete_journalist(id:int):
    for saved_journalist in journalist_list:
        if saved_journalist.id==id:
            journalist_list.remove(saved_journalist)
            return {"message":"Journalist deleted"}
    raise HTTPException(status_code=404, detail="Journalist not found")

#-----------------------

def search_journalist(id_journalist: int):
    journalists = [journalist for journalist in journalist_list if journalist.id == id_journalist]
    
    if not journalists:
        raise HTTPException(status_code=404, detail="Journalist not found")
    return journalists[0]


def next_id():

    return (max(journalist_list, key=id).id+1)