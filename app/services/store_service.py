from sqlalchemy.ext.asyncio import AsyncSession 
from app.schemas.store_schema import CreateStore , ResponseStore , UpdateStore
from app.repository.store_repository import create_store , get_store , get_stores , update_store

from app.models.store_model import Store
from fastapi import HTTPException
from app.models.user_model import User 
from app.repository.locality_repository import get_area





async def making_store(db: AsyncSession,post: CreateStore, current_user: User):
    if current_user.role != "owner": raise HTTPException( status_code=403,detail="Only owners can create stores."  )
    locality = await get_area(db,post.locality_id)
    if locality is None:
        raise HTTPException(   status_code=404,detail="Locality not found." )
    store = Store(
        store_name=post.store_name,
        shop_type=post.shop_type,
        address=post.address,
        description=post.description,
        owner_id=current_user.user_id,
        locality_id=post.locality_id
    )
    return await create_store(db, store)

async def read_store(db:AsyncSession , id:int):
    result=await get_store(db , id)
    if result is None:
        raise HTTPException(status_code=404  , detail="No such Store is Found")
    return result

async def read_stores(db:AsyncSession):
    result =await get_stores(db)
    return result

async def updating_store(db:AsyncSession, id:int, post:UpdateStore, current_user:User):
    if current_user.role != "owner":
        raise HTTPException(status_code=403, detail="Only owners can update stores.")
    store = await get_store(db, id)

    if store is None:
        raise HTTPException(status_code=404, detail="Store not found.")
    if store.owner_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="You are not the owner of this store.")
    
    locality = await get_area(db, post.locality_id)
    if locality is None:
        raise HTTPException(status_code=404, detail="Locality not found.")

    store.store_name = post.store_name
    store.shop_type = post.shop_type
    store.address = post.address
    store.description = post.description
    store.locality_id = post.locality_id

    return await update_store(db, store)

async def removing_store(db:AsyncSession, id:int, current_user:User):
    if current_user.role != "owner":
        raise HTTPException(status_code=403, detail="Only owners can delete stores.")

    store = await get_store(db, id)

    if store is None:
        raise HTTPException(status_code=404, detail="Store not found.")

    if store.owner_id != current_user.user_id:
        raise HTTPException(status_code=403, detail="You are not the owner of this store.")

    return await remove_store(db, store)

    


   


    



