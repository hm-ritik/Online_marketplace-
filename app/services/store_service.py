from sqlalchemy.ext.asyncio import AsyncSession 
from app.schemas.store_schema import CreateStore , ResponseStore , UpdateStore
from app.repository.store_repository import create_store , get_store , get_stores , update_store
from app.models.store_model import Store
from fastapi import HTTPException


async def making_store(db:AsyncSession , post:CreateStore):
    store=Store(
       store_name=post.store_name,
       shop_type=post.shop_type,
       address=post.address,
       description=post.description,
       owner_id=post.owner_id,
       locality_id=post.locality_id
    )
    return await create_store(db , store)

async def read_store(db:AsyncSession , id:int):
    result=await get_store(db , id)
    if result is None:
        raise HTTPException(status_code=404  , detail="No such Store is Found")
    return result

async def read_stores(db:AsyncSession):
    result =await get_stores(db)
    return result

async def updating_store(db:AsyncSession , id:int , post:UpdateStore):
    store=await get_store(db , id)
    if store is None:
        raise HTTPException(status_code=404 , detail="No such store exists")
    store.store_name=post.store_name
    store.shop_type=post.shop_type
    store.address=post.address
    store.description=post.description
    return await update_store (db , store)

    


   


    



