from fastapi import APIRouter , Depends 
from app.models.locality_model import Locality
from app.schemas.locality_schema import CreateLocality , ResponseLocality 
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.services.locality_service import   getall_localities  , get_local , removing_locality , making_locality , updating_locality
from app.dependencies.auth import get_current_user
from app.models.user_model import User


router=APIRouter(prefix="/locality")

@router.post("/locality")
async def create_locality(post:CreateLocality , db:AsyncSession=Depends(get_db),current_user:User=Depends(get_current_user)):
    return await making_locality(db,post,current_user )

@router.put("/updateting")
async def update_locality( post:CreateLocality ,id:int, db:AsyncSession=Depends(get_db) , current_user:User=Depends(get_current_user)):
    return await  updating_locality(db ,id, post,current_user) 


@router.get("/locality{l_id}")
async def get_locality(l_id:int , db:AsyncSession=Depends(get_db)):
    return await get_local(db,l_id)

@router.delete("/remove")
async def delete_locality(id:int, db:AsyncSession=Depends(get_db), current_user:User=Depends(get_current_user)):
    return await removing_locality(db, id, current_user)






