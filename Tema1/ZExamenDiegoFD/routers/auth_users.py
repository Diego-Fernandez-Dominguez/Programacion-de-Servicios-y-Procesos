from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import jwt

from jwt.exceptions import InvalidTokenError, PyJWTError

from pwdlib import PasswordHash

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 1

SECRET_KEY = "87ab51098990feb4a2f78da9c911187a71290ebd9e98e56d8b24090815f2ce6f"

password_hash = PasswordHash.recommended()

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    fullname:str
    email:str
    disabled: bool | None = False

class UserDB(User):
    hashed_password: str


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "fullname": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False
    }
}

def search_user_db(username: str):
    if username in fake_users_db:
        return UserDB(fake_users_db[username])

async def auth_user(token:str = Depends(oauth2)):  

    exception = HTTPException(status_code=401, 
        detail="Credenciales de autenticación inválidas", 
        headers={"WWW-Authenticate" : "Bearer"})
     
    try:        
       
        username = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM).get("sub")

        if username is None:

            raise HTTPException(status_code=401, 
                detail="Credenciales de autenticación inválidas", 
                headers={"WWW-Authenticate" : "Bearer"})       
    except PyJWTError:

        raise HTTPException(status_code=401, 
            detail="Credenciales de autenticación inválidas", 
            headers={"WWW-Authenticate" : "Bearer"})
        

    user = User(**fake_users_db[username])

    if user.disabled:

        raise HTTPException(status_code=400, 
            detail="Usuario inactivo")   

    return user


@router.post("/register", status_code=201)
async def register_user(user: UserDB):
    print("entro en el registro")

    new_password = password_hash.hash(user.hashed_password)
    user.hashed_password = new_password
    fake_users_db[user.username] = user.model_dump()
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):    

    user_db = fake_users_db.get(form.username)   

    if not user_db:
        raise HTTPException(status_code = 400, detail="Usuario no encontrado")

    user = UserDB(**fake_users_db[form.username])

    if not password_hash.verify(form.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="La contraseña no es correcta")  

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = {"sub" : user.username, "exp":expire}
    
    token = jwt.encode(access_token, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token" : token, "token_type": "bearer"}

@router.get("/auth/me")
async def me(user: User = Depends(auth_user)):
    return user