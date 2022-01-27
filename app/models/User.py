from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    email = Column(String(100), unique=True)
    passwd = Column(String(30))
    admin = Column(Boolean)