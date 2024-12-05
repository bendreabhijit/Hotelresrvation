from sqlalchemy.orm import Session
from app import models, schemas
from app.models.room import Room


# Create a room
def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(
        hotel_id=room.hotel_id,
        isSmokingFriendly=room.isSmokingFriendly,
        room_number=room.room_number,
        room_type=room.room_type,
        price=room.price,
        is_available=room.is_available,
        is_cooled=room.is_cooled,
        bed_size=room.bed_size,
        is_gallery=room.is_gallery
    )
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def get_room(db: Session):
    return db.query(Room).all()

# Get room by ID
def get_room_by_id(db: Session, room_id: int):
    return db.query(models.Room).filter(models.Room.id == room_id).first()

# Update room
def update_room(db: Session, room_id: int, room: schemas.RoomUpdate):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room:
        if room.isSmokingFriendly:
            db_room.isSmokingFriendly = room.isSmokingFriendly
        if room.room_number:
            db_room.room_number = room.room_number
        if room.room_type:
            db_room.room_type = room.room_type
        if room.price:
            db_room.price = room.price
        if room.is_available is not None:
            db_room.is_available = room.is_available
        if room.is_cooled is not None:
            db_room.is_cooled = room.is_cooled
        if room.bed_size:
            db_room.bed_size = room.bed_size
        if room.is_gallery is not None:
            db_room.is_gallery = room.is_gallery

        db.commit()
        db.refresh(db_room)
        return db_room
    return None

# Delete room
def delete_room(db: Session, room_id: int):
    db_room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if db_room:
        db.delete(db_room)
        db.commit()
        return db_room
    return None
