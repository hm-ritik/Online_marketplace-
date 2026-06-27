from pydantic  import BaseModel , Field , ConfigDict


class CreateLocality(BaseModel):
    area_name:str
    city:str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)

class UpdateLocality(BaseModel):
    area_name:str
    city:str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class ResponseLocality(BaseModel):
    l_id:int
    area_name:str
    city:str
    latitude:float
    longitude:float
    
    model_config = ConfigDict(from_attributes=True)





