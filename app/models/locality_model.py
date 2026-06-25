from sqlalchemy import Column , String , Integer   , Numeric
from app.core.database import Base


class Locality(Base):
    __tablename__="localities"
    l_id=Column(Integer , primary_key=True , autoincrement=True)
    area_name=Column(String(30) , nullable=False)
    city=Column(String(30) , nullable=False)
    latitude = Column(Numeric(10, 7))
    longitude = Column(Numeric(10, 7))

