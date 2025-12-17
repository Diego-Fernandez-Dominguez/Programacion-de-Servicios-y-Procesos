from typing import Optional
from pydantic import BaseModel

# Entidad journalist
class Journalist(BaseModel):
    id: Optional[str] = None
    name: str
    surname: str
    age: int
