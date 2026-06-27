from app.schemas.store_schema import CreateStore , ResponseStore , UpdateStore
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

async def get_stores(db:AsyncSession):
    result=await db.execute(select(Store))
    return result.scalars().all()

async def update_store(db:AsyncSession , post:UpdateStore):
    await db.commit()
    await db.refresh(post)
    return post 

async def remove_store(db:AsyncSession, store:Store):
    await db.delete(store)
    await db.commit()
    return {"message":"Store deleted successfully."}


