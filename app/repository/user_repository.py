from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy import select
from app.schemas.user_schema import UserCreate , UserResponse
from app.models.user_model import User


async def user_registration(db:AsyncSession , post:UserCreate):
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post
    
async def get_userby_mobileno(db:AsyncSession , mobile_no:str):
    result=await db.execute(select(User).where(User.mobile_no==mobile_no))
    return  result.scalar_one_or_none()

async def get_userbyid(db:AsyncSession , id:int):
    result=await db.execute(select(User).where(User.user_id==id))
    return result.scalar_one_or_none()



async def update_userinfo(db: AsyncSession, user: User):
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_email(db: AsyncSession,email: str):
    result = await db.execute(select(User).where(User.email_id == email))
    return result.scalar_one_or_none()

async def get_user_by_mobileno(db:AsyncSession , mobile_no:str):
    result=await db.execute(select(User).where(User.mobile_no==mobile_no))
    return result.scalar_one_or_none()

"""async def remove_user(db:AsyncSession , post:UserResponse):
        await db.delete(post)
        await db.commit()"""
  

  
 
    
    
    


