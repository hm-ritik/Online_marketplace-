from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.locality_schema import CreateLocality , ResponseLocality  , UpdateLocality
from app.repository.locality_repository import get_by_name
from fastapi import HTTPException
from app.models.locality_model import Locality
from app.repository.locality_repository import create_locality ,getall_area , updateinfo , get_area , remove_locality
from app.models.user_model import User


async def making_locality(db:AsyncSession, post:CreateLocality, current_user:User):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can create locality.")

    locality = Locality(
        area_name=post.area_name,
        city=post.city,
        latitude=post.latitude,
        longitude=post.longitude
    )

    return await create_locality(db, locality)

async def getall_localities(db:AsyncSession):
    return await getall_area(db)

async def updating_locality(db:AsyncSession, id:int, post:UpdateLocality, current_user:User):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can update locality.")

    locality = await get_area(db, id)

    if locality is None:
        raise HTTPException(status_code=404, detail="Locality not found.")

    locality.area_name = post.area_name
    locality.city = post.city
    locality.latitude = post.latitude
    locality.longitude = post.longitude

    return await updateinfo(db, locality)

async def get_local(db:AsyncSession , l_id:int):
    result=await get_area(db , l_id)
    if result is None:
        raise HTTPException(status_code=404 , detail="Area Do Not Exists")
    return result

async def removing_locality(db:AsyncSession, id:int, current_user:User):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Only admins can delete locality.")

    locality = await get_area(db, id)

    if locality is None:
        raise HTTPException(status_code=404, detail="Locality not found.")

    return await remove_locality(db, locality)

    





