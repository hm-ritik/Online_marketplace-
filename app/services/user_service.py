from sqlalchemy.ext.asyncio import AsyncSession 
from app.schemas.user_schema import UserCreate , UserResponse , UserUpdate , Login
from app.repository.user_repository import user_registration , get_userby_mobileno ,get_userbyid  , update_userinfo , get_user_by_email , get_user_by_mobileno #, remove_user
from fastapi import HTTPException
from app.models.user_model import User
from app.core.security import hashing_password , verifying_password , create_access_token



async def register_user(db:AsyncSession , post:UserCreate):
    existing_user=await get_userby_mobileno(db , post.mobile_no)
    if existing_user:
        raise HTTPException(status_code=409 , detail="Mobile_No already exists")
    password=hashing_password(post.hashed_password)
    user=User(
       name=post.name,
       mobile_no=post.mobile_no,
       email_id=post.email_id,
       role=post.role,
       hashed_password=password
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


async def login_user( db: AsyncSession,post: Login):
    if "@" in post.identifier:
        user = await get_user_by_email(db,post.identifier)
    else:
        user = await get_user_by_mobileno(db,post.identifier)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verifying_password(
        post.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    token = create_access_token(
        {"sub": str(user.user_id)}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }



"""async def delete_userinfo(db:AsyncSession , id:int):
    user= await get_userbyid(db , id)
    if user is None:
        raise HTTPException(status_code=404 , detail="user do not exists")
    return await remove_user(db ,user)"""





    
    


    
        