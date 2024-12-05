from pydantic import BaseModel
from typing import Optional

class RoomCreate(BaseModel):
    hotel_id: int
    isSmokingFriendly: bool
    room_number: str
    room_type: Optional[str] = None
    price: float
    is_available: Optional[bool] = True
    is_cooled: Optional[bool] = False
    bed_size: Optional[str] = None
    is_gallery: Optional[bool] = False

class RoomUpdate(BaseModel):
    isSmokingFriendly: Optional[bool] = None
    room_number: Optional[str] = None
    room_type: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None
    is_cooled: Optional[bool] = None
    bed_size: Optional[str] = None
    is_gallery: Optional[bool] = None


class RoomUpdateResponse(BaseModel):
    message: str

class RoomResponse(RoomCreate):
    id: int

    class Config:
        from_attributes = True  # Ensures compatibility with SQLAlchemy model
