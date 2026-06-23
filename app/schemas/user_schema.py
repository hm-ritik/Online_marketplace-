from pydantic import BaseModel , EmailStr , Field ,  ConfigDict , field_validator
from datetime import datetime 
import re 



class UserCreate(BaseModel):
    name:str =Field(min_length=3 , max_length=15)
    