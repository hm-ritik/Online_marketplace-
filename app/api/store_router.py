from fastapi import Depends , APIRouter 
from app.schemas.store_schema import CreateStore , ResponseStore
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.store_service import making_store , read_store


router=APIRouter(prefix="/store")

@router.post("/store", response_model=ResponseStore)
async def make_store(post:CreateStore , db:AsyncSession=Depends(get_db)):
    return await making_store(db ,post )

@router.get("/getstore",response_model=ResponseStore)
async def store(id:int , db:AsyncSession=Depends(get_db)):
    return await read_store(db , id)