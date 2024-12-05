# app/schemas/reservation.py
from pydantic import BaseModel
from datetime import date, time

class ReservationBase(BaseModel):
    hotel_id:int
    room_id: int
    customer_id: int
   
    check_in_date: date
    check_out_hour: int  

class ReservationCreate(ReservationBase):
    pass

class ReservationUpdate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int
    bookingID:str

    class Config:
        from_attributes = True  # Use 'from_attributes' instead of 'orm_mode' in Pydantic v2
