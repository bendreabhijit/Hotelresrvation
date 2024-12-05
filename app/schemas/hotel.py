from pydantic import BaseModel
from typing import Optional
from typing import List

class HotelCreate(BaseModel):
    branch: str
    pincode: str
    locality: str
    manager: str

class HotelUpdate(BaseModel):
    branch: Optional[str] = None
    pincode: Optional[str] = None
    locality: Optional[str] = None
    manager: Optional[str] = None

class RoomResponse(BaseModel):
    hotel_id: int
    isSmokingFriendly: bool
    room_number: str
    room_type: Optional[str] = None
    price: float
    is_available: Optional[bool] = True
    is_cooled: Optional[bool] = False
    bed_size: Optional[str] = None
    is_gallery: Optional[bool] = False
     

class hotelLocationResponse(HotelCreate):
     rooms: List[RoomResponse] 



class HotelResponse(HotelCreate):
    id: int
   

    class Config:
        from_attributes = True


