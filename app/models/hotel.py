from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    branch = Column(String(100))
    pincode = Column(String(6))
    locality = Column(String(100))
    manager = Column(String(100))

    # Optionally, you can add a relationship with Room, assuming rooms belong to a hotel
    rooms = relationship("Room", back_populates="hotel")