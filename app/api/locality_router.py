from fastapi import APIRouter , Depends 
from app.models.locality_model import Locality
from app.schemas.locality_schema import CreateLocality , ResponseLocality 
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.locality_service import  create_area , getall_localities , update_area , get_local


router=APIRouter(prefix="/locality")

@router.post("/locality")
async def create_locality(post:CreateLocality , db:AsyncSession=Depends(get_db)):
    return await create_area(db,post)

@router.get("/localities")
async def get_localities(db:AsyncSession=Depends(get_db)):
    return await getall_localities(db)

@router.put("/updateting")
async def update_locality( post:CreateLocality , db:AsyncSession=Depends(get_db)):
    return await   update_area(db ,post) 

@router.get("/locality{l_id}")
async def get_locality(l_id:int , db:AsyncSession=Depends(get_db)):
    return await get_local(db,l_id)




