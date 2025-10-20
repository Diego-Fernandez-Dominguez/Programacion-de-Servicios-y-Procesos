from fastapi import FastAPI
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
           Journalist(id=3 ,dni="11223344C", name="Luis", surname="Garcia", telephone=698765432, specialty="Culture")]


# Get all journalists
@app.get("/journalists/")
def get_journalists():
    return journalist_list

# Id
@app.get("/journalists/id/{id_journalist}")
def get_journalist_by_id(id_journalist: int):
    journalist = next((j for j in journalist_list if j.id == id_journalist), None)
    if journalist:
        return journalist
    return {"error": "Journalist with that ID not found"}

# DNI
@app.get("/journalists/dni/{dni}")
def get_journalist_by_dni(dni: str):
    journalist = next((j for j in journalist_list if j.dni.lower() == dni.lower()), None)
    if journalist:
        return journalist
    return {"error": "Journalist with that DNI not found"}

# Name
@app.get("/journalists/name/{name}")
def get_journalists_by_name(name: str):
    results = [j for j in journalist_list if j.name.lower() == name.lower()]
    return results if results else {"error": "No journalists found with that name"}

# Surname
@app.get("/journalists/surname/{surname}")
def get_journalists_by_surname(surname: str):
    results = [j for j in journalist_list if j.surname.lower() == surname.lower()]
    return results if results else {"error": "No journalists found with that surname"}

# Telephone
@app.get("/journalists/telephone/{telephone}")
def get_journalists_by_telephone(telephone: int):
    results = [j for j in journalist_list if j.telephone == telephone]
    return results if results else {"error": "No journalists found with that telephone number"}

# Specialty
@app.get("/journalists/specialty/{specialty}")
def get_journalists_by_specialty(specialty: str):
    results = [j for j in journalist_list if j.specialty.lower() == specialty.lower()]
    return results if results else {"error": "No journalists found with that specialty"}