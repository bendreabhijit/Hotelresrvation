from sqlalchemy.orm import Session
from app import models, schemas

# Create a new hotel
# In app/crud/hotel.py

def create_hotel(db: Session, hotel: "schemas.HotelCreate"):
    from app import schemas  # Delayed import to avoid circular import
    new_hotel = schemas.Hotel(**hotel.dict())
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)
    return new_hotel


# Get all hotels
def get_hotels(db: Session):
    from app import schemas  
    from . import models
    return db.query(models.Hotel).all()

# Get a hotel by ID



# Function to get a hotel by its ID
def get_hotel(db: Session, hotel_id: int):
    from . import models
    from app import schemas  
    return db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()

def get_hotelbylocation(db: Session, branch: str):
    from . import models
    from app import schemas  
    return db.query(models.Hotel).filter(models.Hotel.branch == branch).all()


def update_hotel(db: Session, hotel_id: int, hotel: schemas.HotelUpdate):
    from app import schemas  
    db_hotel = db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
    if db_hotel:
        if hotel.branch:
            db_hotel.branch = hotel.branch
        if hotel.pincode:
            db_hotel.pincode = hotel.pincode
        if hotel.locality:
            db_hotel.locality = hotel.locality
        if hotel.manager:
            db_hotel.manager = hotel.manager

        db.commit()
        db.refresh(db_hotel)
        return db_hotel
    return None



# from sqlalchemy.orm import Session
# from app import models

def delete_hotel(db: Session, hotel_id: int):
    db_hotel = db.query(models.Hotel).filter(models.Hotel.id == hotel_id).first()
    if db_hotel:
        db.delete(db_hotel)
        db.commit()
        return db_hotel
    return None
