from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, Time
from sqlalchemy.orm import relationship
from app.database import Base

class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True, index=True)
    hotel_id=Column(Integer, ForeignKey("hotels.id"))    
    room_id = Column(Integer, ForeignKey("rooms.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    check_in_date = Column(DateTime, default=datetime.utcnow)  # Use date or datetime in production
    check_out_date = Column(DateTime, default=datetime.utcnow)   
    bookingID  =Column(Integer,index=True)   
    
    customer = relationship("Customer", back_populates="reservations")
    room = relationship("Room")
