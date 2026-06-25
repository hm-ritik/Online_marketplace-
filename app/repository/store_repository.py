from app.schemas.store_schema import CreateStore , ResponseStore
from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession 
from sqlalchemy import select 
from app.models.store_model import Store





async def create_store(db:AsyncSession , post:CreateStore):
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post

async def get_store(db:AsyncSession , id:int):
    result= await db.execute(select(Store).where(Store.store_id==id))
    return result.scalar_one_or_none()
