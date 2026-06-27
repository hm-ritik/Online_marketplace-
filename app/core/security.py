from passlib.context import CryptContext
from jose import jwt , JWTError
from datetime import datetime , timedelta
from dotenv import load_dotenv
import os 
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends , HTTPException 
from app.core.database import get_db
from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user_model import User





load_dotenv()
SECRET_KEY=os.getenv("JWT_SECRET_KEY")
ALGORITHM="HS256"
TIME_IN_MINUTES=20


pwd_context=CryptContext(schemes=["bcrypt"] , deprecated="auto")
def hashing_password(password:str):
    hashed_password=pwd_context.hash(password)
    return hashed_password

def verifying_password(plain_password:str , hashed_password:str):
    verified_password=pwd_context.verify(plain_password , hashed_password)
    return verified_password

def create_access_token(sub:dict):
    to_encode=sub.copy()
    expire=datetime.utcnow() + timedelta(minutes=TIME_IN_MINUTES)
    to_encode.update(
        {
            "exp":expire
        }
    )
    token=jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)
    return token


