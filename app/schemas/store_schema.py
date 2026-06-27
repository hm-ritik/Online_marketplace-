from pydantic import BaseModel , ConfigDict  , Field 
from typing import Literal

class CreateStore(BaseModel):
    store_name: str = Field(min_length=2, max_length=100)
    shop_type: Literal['Kirana' , 'Clothes' , 'Medical' , 'Salon']
    address: str = Field(min_length=5, max_length=200)
    description: str = Field(min_length=10, max_length=500)
    locality_id:int

class UpdateStore(BaseModel):
     store_name:str
     shop_type:Literal['Kirana' , 'Clothes' , 'Medical' , 'Salon']
     address:str
     description:str    

class ResponseStore(BaseModel):
    store_id:int
    store_name:str
    shop_type:Literal['Kirana' , 'Clothes' , 'Medical' , 'Salon']
    address:str
    description:str
    owner_id:int
    locality_id:int
    model_config = ConfigDict(from_attributes=True)











