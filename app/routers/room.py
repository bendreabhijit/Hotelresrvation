from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.room import Room
from app.schemas.room import RoomCreate, RoomResponse,RoomUpdateResponse
from app.database import get_db
from app import crud, schemas, database

router = APIRouter()

# Create a new room
@router.post("/rooms/", response_model=schemas.RoomResponse)
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.create_room(db=db, room=room)

# Get all rooms
@router.get("/rooms/")
def get_rooms(db: Session = Depends(get_db)):
    return crud.get_room(db=db)


# Get a room by ID
@router.get("/rooms/{room_id}", response_model=schemas.RoomResponse)
def get_room_by_id(room_id: int, db: Session = Depends(get_db)):
    db_room = crud.get_room_by_id(db=db, room_id=room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

# Update a room
@router.put("/rooms/{room_id}", response_model=schemas.RoomUpdateResponse)
def update_room(room_id: int, room: schemas.RoomUpdate, db: Session = Depends(get_db)):
    db_room = crud.update_room(db=db, room_id=room_id, room=room)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    
    return {"message": " Room updated successfully !"}

# Delete a room
@router.delete("/rooms/{room_id}")
def delete_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found") 
    
    db.delete(room)
    db.commit()    
    return {"message": "Room deleted successfully!"}