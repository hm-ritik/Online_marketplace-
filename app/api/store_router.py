from fastapi import Depends , APIRouter 
from app.schemas.store_schema import CreateStore , ResponseStore , UpdateStore
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.store_service import making_store , read_store , read_stores , updating_store , removing_store
from app.dependencies.auth import get_current_user
from app.models.user_model import User


router=APIRouter(prefix="/store")

@router.post("/store", response_model=ResponseStore)
async def make_store(post:CreateStore , db:AsyncSession=Depends(get_db) , current_user:User=Depends(get_current_user)):
    return await making_store(db ,post , current_user)

@router.get("/getstore",response_model=ResponseStore)
async def store(id:int , db:AsyncSession=Depends(get_db)):
    return await read_store(db , id)

@router.get("/stores", response_model=list[ResponseStore])
async def stores(db:AsyncSession=Depends(get_db)):
    return await read_stores(db)

@router.put("/change",response_model=ResponseStore)
async def update_store(id:int , post:UpdateStore , db:AsyncSession=Depends(get_db),current_user: User = Depends(get_current_user)):
    return await updating_store(db , id , post,current_user)

@router.delete("/remove")
async def delete_store(id:int, db:AsyncSession=Depends(get_db), current_user:User=Depends(get_current_user)):
    return await removing_store(db, id, current_user)


 