from app.core.database import  get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter , Depends
from app.schemas.user_schema import UserCreate , UserResponse , UserUpdate
from app.services.user_service import register_user , get_user , update_user



router = APIRouter( prefix="/users")

@router.post("/register",response_model=UserResponse)
async def registration(post:UserCreate ,db:AsyncSession=Depends(get_db)):
    return await register_user(db , post)

@router.get("/getuser",response_model=UserResponse)
async def get_userdetail(mobile_no:str ,db:AsyncSession=Depends(get_db)):
    return await get_user(db,mobile_no)


@router.put("/updateinfo/{user_id}", response_model=UserResponse)
async def updating_user(user_id: int, post: UserUpdate, db: AsyncSession = Depends(get_db)):
    return await update_user(db, user_id, post)


