from sqlalchemy.ext.asyncio import AsyncSession 
from app.schemas.user_schema import UserCreate , UserResponse , UserUpdate
from app.repository.user_repository import user_registration , get_userby_mobileno ,get_userbyid  , update_userinfo
from fastapi import HTTPException
from app.models.user_model import User



async def register_user(db:AsyncSession , post:UserCreate):
    existing_user=await get_userby_mobileno(db , post.mobile_no)
    if existing_user:
        raise HTTPException(status_code=409 , detail="Mobile_No already exists")
    user=User(
       name=post.name,
       mobile_no=post.mobile_no,
       email_id=post.email_id,
       role=post.role
    )
    return await user_registration(db,user)

async def get_user(db:AsyncSession , mobile_no:str):
    user=await get_userby_mobileno(db ,mobile_no)
    if not user:
        raise HTTPException(status_code=409, detail="Mobile_No already exists")
    return  user


async def update_user(db: AsyncSession, user_id: int, post: UserUpdate):
    user = await get_userbyid(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = post.name
    user.mobile_no = post.mobile_no
    user.email_id = post.email_id
    return await update_userinfo(db, user)



    
    


    
        