from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserDTO(BaseModel):
    id: Optional[int]
    name: str
    email: str

    class Config:
        orm_mode = True


class User(Base):
    _tablename_ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)