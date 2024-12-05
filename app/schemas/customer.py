from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    age: int
    email: str
    phone_number: str  # Primary key will be used here
    traveling_from: Optional[str] = None
    isForeign: bool = False
    purpose: str
    room_id:int

    class Config:
        from_attributes = True  # Pydantic v2 compatibility


class CustomerCreate(CustomerBase):
    pass  # No changes required for the creation model, just reusing CustomerBase

#*****************************************************************************************************
#   JSON ENDPOINT TO ADD THREE TABLES AT A TIME 
# ****************************************************************************************************
class HotelCreate(BaseModel):
    branch: str
    pincode: str
    locality: str
    manager: str

class RoomCreate(BaseModel):
    hotel_id: int
    name: str
    room_number: str
    room_type: Optional[str] = None
    price: float
    is_available: Optional[bool] = True
    is_cooled: Optional[bool] = False
    bed_size: Optional[str] = None
    is_gallery: Optional[bool] = False



class CustomerCreateRoomHobby(BaseModel):
    name: str
    age: int
    email: EmailStr
    phone_number: str  # Primary key will be used here
    traveling_from: Optional[str] = None
    isForeign: bool = False
    purpose: str
    room: RoomCreate
    hotel: HotelCreate
    

class CustomerResponse(CustomerBase):
    id:int

    class Config:
        from_attributes = True  # Pydantic v2 compatibility

#************************************************************************************************************
#************************************************************************************************************
class CustomerUpdate(BaseModel):
    name: Optional[str]
    age: Optional[int]
    email: Optional[str]
    phone_number: Optional[str]
    traveling_from: Optional[str]
    isForeign: Optional[bool]
    purpose: Optional[str]

    class Config:
        from_attributes = True
