from sqlalchemy import Column , String , Integer   , Decimal , ForeignKey , DateTime

from app.core.database import Base
from app.models import locality_model
from datetime import datetime


class Store(Base):
    __tablename__="stores"
    store_id=Column(Integer , primary_key=True , autoincrement=True)
    store_name=Column(String , nullable=False)
    shop_type=Column(String , nullable=False)
    address=Column(String(40))
    description=Column(String(150) , nullable=False)
    owner_id = Column(Integer, ForeignKey("users.user_id"))
    locality_id = Column(Integer, ForeignKey("localities.l_id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    