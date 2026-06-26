from pydantic import BaseModel , EmailStr , Field ,  ConfigDict , field_validator
from datetime import datetime 
import re 
from typing import Literal



class UserCreate(BaseModel):
    name:str =Field(min_length=3 , max_length=15)
    mobile_no:str
    email_id: EmailStr 
    role: Literal["owner", "user"]
    hashed_password:str=Field(min_length=6 , max_length=15)
    

    @field_validator("mobile_no")
    @classmethod
    def phone_must_be_valid(cls, v):
        if not re.match(r"^[6-9]\d{9}$", v):
            raise ValueError("Enter a valid 10 digit Indian mobile number")
        return v
    
class UserResponse(BaseModel):
    user_id:int
    name:str
    mobile_no:str
    email_id: EmailStr 
    role: Literal['owner' , 'user']    

    
   

class UserUpdate(BaseModel):
    name: str
    mobile_no: str
    email_id: EmailStr
    model_config = ConfigDict(from_attributes=True)




