from jose import JWTError, jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import SECRET_KEY, ALGORITHM
from app.repository.user_repository import get_userbyid

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

async def get_current_user(token: str = Depends(oauth2_scheme),db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        user_id = int(user_id)
    except JWTError:
        raise credentials_exception
    user = await get_userbyid(db, user_id)
    if user is None:
        raise credentials_exception
    return user