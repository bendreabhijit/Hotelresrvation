from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Room(Base):
    __tablename__ = "rooms"
    
    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    isSmokingFriendly = Column(Boolean, nullable=False)  
    room_number = Column(String(255), index=True)
    room_type = Column(String(255))  # Type of room, such as "Single", "Double", etc.
    price = Column(Float)
    is_available = Column(Boolean, default=True)  # Whether the room is available or not
    is_cooled = Column(Boolean, default=False)  # Whether the room has air conditioning
    bed_size = Column(String(50))  # Size of the bed, e.g., "King", "Queen", etc.
    is_gallery = Column(Boolean, default=False)  # Whether the room has access to a gallery
    hotel_id = Column(Integer, ForeignKey("hotels.id"))

    hotel = relationship("Hotel", back_populates="rooms")
    customers = relationship("Customer", back_populates="room")