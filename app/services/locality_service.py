from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.locality_schema import CreateLocality , ResponseLocality 
from app.repository.locality_repository import get_by_name
from fastapi import HTTPException
from app.models.locality_model import Locality
from app.repository.locality_repository import register_locality ,getall_area , updateinfo , get_area


async def create_area(db:AsyncSession , post:CreateLocality):
    area=await get_by_name(db , post.area_name)
    if  area:
        raise HTTPException(status_code=409 , detail="Area Already Exist")
    area=Locality( area_name=post.area_name, city=post.city, latitude=post.latitude,longitude=post.longitude)
    return await register_locality(db , area)

async def getall_localities(db:AsyncSession):
    return await getall_area(db)

async def update_area(db:AsyncSession , post:CreateLocality):
    area=await get_by_name(db , post.area_name)
    if not  area:
        raise HTTPException(status_code=404 , detail="Wrong Info Area do not exists")
    area.area_name=post.area_name
    area.city=post.city
    area.latitude=post.latitude
    area.longitude=post.longitude
    return await updateinfo(db , area)

async def get_local(db:AsyncSession , l_id:int):
    result=await get_area(db , l_id)
    if result is None:
        raise HTTPException(status_code=404 , detail="Area Do Not Exists")
    return result

    





