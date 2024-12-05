from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import role_required
from app.models.hotel import Hotel
from app.schemas.hotel import HotelResponse, HotelCreate, HotelUpdate ,hotelLocationResponse # Add other necessary imports
from app.database import get_db
from app import crud, database 
from typing import List

router = APIRouter()

@router.get("/admin-only")
def get_admin_data(current_role: str = Depends(role_required("admin"))):
    return {"message": "This is a restricted admin-only route."}

@router.post("/hotels/", response_model=HotelResponse)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    db_hotel = db.query(Hotel).filter(Hotel.locality == hotel.locality).first()
    if db_hotel:
        raise HTTPException(status_code=400, detail="Hotel already exists")
    new_hotel = Hotel(**hotel.dict())  # Create a new hotel using HotelCreate model data
    db.add(new_hotel)
    db.commit()
    db.refresh(new_hotel)
    return new_hotel  # Returning the created hotel data

@router.put("/{hotel_id}", response_model=HotelResponse)
def update_hotel(
    hotel_id: int, hotel: HotelUpdate, db: Session = Depends(get_db)
):
    # Fetch the hotel by its ID
    db_hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()

    # If hotel doesn't exist, raise 404 error
    if not db_hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")

    # Update the hotel's details with the provided values
    if hotel.branch:
        db_hotel.branch = hotel.branch
    if hotel.pincode:
        db_hotel.pincode = hotel.pincode
    if hotel.locality:
        db_hotel.locality = hotel.locality
    if hotel.manager:
        db_hotel.manager = hotel.manager
    
    # Commit the changes to the database
    db.commit()

    # Refresh the object to reflect the updated data
    db.refresh(db_hotel)

    # Return the updated hotel data
    return db_hotel

# Get all hotels
@router.get("/hotels/", response_model=list[HotelResponse])
def get_hotels(db: Session = Depends(get_db)):
    from . import models
    hotels = db.query(Hotel).all()
    return hotels


@router.get("/hotels/{hotel_id}", response_model=HotelResponse)  # Correct schema
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    from . import models  #importing here to avoid circular imports 
    db_hotel = crud.get_hotel(db=db, hotel_id=hotel_id)  # Call to your CRUD function
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return db_hotel


@router.get("/hotels/location/{location}", response_model=List[hotelLocationResponse])
def get_hotelbylocation(location: str, db: Session = Depends(get_db)):
    db_hotel = crud.get_hotelbylocation(db=db, branch=location)
    if db_hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return db_hotel


@router.delete("/{hotel_id}")
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    db.delete(hotel)
    db.commit()
    return {"detail": "Hotel deleted"}
