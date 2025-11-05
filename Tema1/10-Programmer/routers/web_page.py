from fastapi import APIRouter, FastAPU, HTTPException
from pydantic import BaseModel

router=APIRouter(prefix="/web_page", tags=["web_pages"])

class Web_Page(BaseModel):
    id:int
    title:str
    theme:str
    url:str
    id_programmer:int

web_pages = [
    Web_Page(id=1, title="TechBlog", theme="Tecnología", url="https://techblog.example.com", id_programmer=1),
    Web_Page(id=2, title="Foodies", theme="Gastronomía", url="https://foodies.example.com", id_programmer=2),
    Web_Page(id=3, title="TravelNow", theme="Viajes", url="https://travelnow.example.com", id_programmer=3),
    Web_Page(id=4, title="FitnessPro", theme="Deporte y Salud", url="https://fitnesspro.example.com", id_programmer=4),
    Web_Page(id=5, title="BookCorner", theme="Literatura", url="https://bookcorner.example.com", id_programmer=5)
]

@router.get("/web_pages")
def web_pages():
    return web_pages