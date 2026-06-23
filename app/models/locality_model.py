from sqlalchemy import Column , String , Integer   , Decimal
from app.core.database import Base


class Locality(Base):
    __tablename__="localities"
    l_id=Column(Integer , primary_key=True , autoincrement=True)
    area_name=Column(String(30) , nullable=False)
    city=Column(String(30) , nullable=False)
    latitude = Column(Decimal(10, 7))
    longitude = Column(Decimal(10, 7))

