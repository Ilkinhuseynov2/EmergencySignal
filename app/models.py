from email.policy import default
from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base

group_users = Table('group_users', Base.metadata,
    Column('group_id', ForeignKey('group.id'), primary_key=True),
    Column('users_id', ForeignKey('users.id'), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique= True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    phone = Column(String, default = ' ')
    group = relationship("Group", back_populates="owner")


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique= True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="group")