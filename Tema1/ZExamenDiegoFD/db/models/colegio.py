from typing import Optional
from pydantic import BaseModel

class Colegio(BaseModel):
    id: Optional[str] = None
    nombre:str
    distrito:float
    tipo:str
    direccion:str
