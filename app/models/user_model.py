from sqlalchemy import Column , String , Integer    , DateTime
from app.core.database import Base
from datetime import datetime

class User(Base):
    __tablename__="users"
    user_id=Column(Integer , primary_key=True , autoincrement=True)
    name=Column(String(15) , nullable=False , unique=True)
    mobile_no=Column(String(15) , nullable=False , unique=True)
    email_id=Column(String(35) )
    role=Column(String(20) , nullable=False)
    hashed_password=Column(String(255),nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)



    

