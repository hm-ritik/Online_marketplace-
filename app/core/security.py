from passlib.context import CryptContext
from jose import jwt


pwd_context=CryptContext(schemes=["bcrypt"] , deprecated="auto")


def hashing_password(password:str):
    hashed_password=pwd_context.hash(password)
    return hashed_password

def verifying_password(plain_password:str , hashed_password:str):
    verified_password=pwd_context.verify(plain_password , hashed_password)
    return verified_password
