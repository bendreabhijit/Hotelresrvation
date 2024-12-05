from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class CustomerCreatefromuser(UserCreate):
    name: str
    age: int  
    phone_number: str   
    traveling_from: Optional[str] = None
    isForeign: bool = False
    purpose: str
    room_id:int

class CreateSystemUser(UserCreate):
    role:str

class UserOut(UserBase):
    id: int     

    class Config:
        from_attributes = True
