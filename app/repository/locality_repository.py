from sqlalchemy.ext.asyncio import AsyncSession 
from app.models.locality_model import Locality 
from sqlalchemy import select
from app.schemas.locality_schema import CreateLocality , ResponseLocality



async def get_by_name(db:AsyncSession , area_name:str):
    result= await db.execute(select(Locality).where(area_name==Locality.area_name))
    return result.scalar_one_or_none()

async def create_locality(db:AsyncSession, locality:Locality):
    db.add(locality)
    await db.commit()
    await db.refresh(locality)
    return locality


async def getall_area(db:AsyncSession):
    result=await db.execute(select(Locality))
    return result.scalars().all()

async def updateinfo(db:AsyncSession , post:CreateLocality):
   
    await db.commit()
    await db.refresh(post)
    return post

async def get_area(db:AsyncSession , id:int):
    result=await db.execute (select(Locality).where(id==Locality.l_id))
    return result.scalar_one_or_none()

async def remove_locality(db:AsyncSession, locality:Locality):
    await db.delete(locality)
    await db.commit()
    return {"message":"Locality deleted successfully."}
