from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

import jwt
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRES_MINUTES=5

SECRET_KEY = "d8697249c68c639a5cde4519905abc74a69ec715d0af38a3845ce56cab516494"

password_hash = PasswordHash.recommended()

router = APIRouter()

class User(BaseModel):
    username : str
    fullname : str
    email : str
    disable : bool

class UserDB(User):
    password:str

users_db = {
    "diegofd" : {
        "username" : "yo :)",
        "fullname" : "pues yo, pero mas largo",
        "email" : "dieogfernandezdominguez406@gmail.com",
        "disable" : False,
        "password" : "alibaba"
    },
    "noir_206" : {
        "username" : "Adriano",
        "fullname" : "Morenito Montador",
        "email" : "noir206@gmail.com",
        "disable" : False,
        "password" : "soyunfemb"
    },
    "pruebota" : {   
        "username": "pruebota",
        "fullname": "pruebotalolazo",
        "email": "correoprueba@gmail.com",
        "disable": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$Yjhn/g3ouDCS/J2PdQQ2rw$gV41w60nuHqTYhgGMShhHrRZ9R8jutOfRiP63SGKCTs"
    }
}


@router.post("/register", status_code=201)
def register(user: UserDB):
    if user.username not in users_db:
        hashed_password=password_hash.hash(user.password)
        user.password=hashed_password
        users_db[user.username] = user
        return user
    else:
        raise HTTPException(status_code = 409, detail="User alredy exists")