from sqlalchemy import Boolean, Column, Integer, String
from ..database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(250), unique=True, index=True)
#     hashed_password = Column(String(250))


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(250), unique=True, index=True, nullable=False)
    password = Column(String(500), nullable=False)
    role = Column(String(250), nullable=False)  # 'customer' or other roles
    is_active = Column(Boolean, default=True)
