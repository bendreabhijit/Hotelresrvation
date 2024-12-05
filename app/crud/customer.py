from sqlalchemy.orm import Session
from app.crud.users import hashed_password
from app.models.customer import Customer
from app.models.users import User
from app.schemas.customer import CustomerBase, CustomerResponse, CustomerCreateRoomHobby
from fastapi import HTTPException
from typing import List, Optional
from sqlalchemy.orm import joinedload

from sqlalchemy.orm import Session
from app.models import Customer, Room, Hotel
from app.schemas import CustomerCreate, RoomCreate, HotelCreate
from app.schemas.users import CustomerCreatefromuser, UserCreate

# Create or get a Hotel
# def get_or_create_hotel(db: Session, hotel_data: HotelCreate):
#     # Check if the hotel already exists by matching the branch (hotel name) and pincode
#     hotel = db.query(Hotel).filter(Hotel.branch == hotel_data.branch, Hotel.locality == hotel_data.locality).first()
    
#     if not hotel:
#         # Create a new hotel if it doesn't exist
#         hotel = Hotel(
#             branch=hotel_data.branch,
#             locality=hotel_data.locality,
#             manager=hotel_data.manager,  # Use manager from the Pydantic model
#             pincode=hotel_data.pincode  # Storing pincode as additional information
#         )
#         db.add(hotel)
#         db.commit()
#         db.refresh(hotel)
    
#     return hotel


# # Create a Room linked to a Hotel
# def create_room(db: Session, room_data: RoomCreate, hotel_id: int):
#     room = Room(
#         name=room_data.name,
#         room_number=room_data.room_number,
#         room_type=room_data.room_type,
#         price=room_data.price,
#         hotel_id=hotel_id
#     )
#     db.add(room)
#     db.commit()
#     db.refresh(room)
#     return room

# # Create a Customer linked to a Room
# def create_customer2(db: Session, customer_data: CustomerCreate, room_id: int):
#     customer = Customer(
#         name=customer_data.name,
#         email=customer_data.email,
#         room_id=room_id
#     )
#     db.add(customer)
#     db.commit()
#     db.refresh(customer)
#     return customer










# Create a new customer
def create_customerwithuser(db: Session,  user_in: CustomerCreatefromuser) -> Customer:
   
    db_user = User(
        email=user_in.email,
        password=hashed_password(user_in.password),
        role="customer",
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)



    db_customer = Customer(

        id=db_user.id
        ,name=user_in.name
        ,age= user_in.age
        ,email= user_in.email
        ,phone_number= user_in.phone_number  # Primary key will be used here
        ,traveling_from= user_in.traveling_from
        ,isForeign= user_in.isForeign
        ,purpose= user_in.purpose
        ,room_id=user_in.room_id
        )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)


    return db_customer


def get_customer_with_room_and_hotel(db: Session, customer_id: int):
    return db.query(Customer).options(
        joinedload(Customer.room).joinedload(Room.hotel)
    ).filter(Customer.id == customer_id).first()


# Get all customers with pagination

def get_customers(db: Session, skip: int = 0, limit: int = 100) -> List[Customer]:
    return db.query(Customer).offset(skip).limit(limit).all()

# Get a customer by ID
def get_customer(db: Session, customer_id: int) -> Customer:
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

# Update a customer by ID
def update_customer(db: Session, customer_id: int, customer: CustomerBase) -> Customer:
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    # Update fields
    for var, value in vars(customer).items():
        if value is not None:
            setattr(db_customer, var, value)

    db.commit()
    db.refresh(db_customer)
    return db_customer

# Delete a customer by ID
def delete_customer(db: Session, customer_id: int) -> Customer:
    db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    
    db.delete(db_customer)
    db.commit()
    return db_customer
