'''For Creating Database Table'''

from sqlalchemy import Column, Integer, String, ForeignKey , Boolean
from .database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    is_admin = Column(Boolean, default=False)

class Organization(Base):
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)