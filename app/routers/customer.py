# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.models.customer import Customer
# from app.schemas.customer import CustomerBase
# from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.customer import create_customerwithuser
from app.models.customer import Customer
from app.models.users import User
from app.schemas.customer import CustomerCreate, CustomerUpdate, CustomerResponse, CustomerCreateRoomHobby
from app.database import get_db
from app import crud
from app.schemas.users import CustomerCreatefromuser 
router = APIRouter()

# @router.post("/", response_model=CustomerResponse)
# def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
#     # Check if a customer with the given phone number already exists
#     existing_customer = db.query(Customer).filter(Customer.phone_number == customer.phone_number).first()
#     if existing_customer:
#         raise HTTPException(status_code=400, detail="Customer with this phone number already exists.")
    
#     db_customer = Customer(**customer.dict())
#     db.add(db_customer)
#     db.commit()
#     db.refresh(db_customer)
    
#     return db_customer

@router.post("/", response_model=CustomerResponse)
def create_customerandUser(customer: CustomerCreatefromuser, db: Session = Depends(get_db)):
    # Check if a customer with the given phone number already exists
    existing_user = db.query(User).filter(User.email == customer.email).first()
    if existing_user:         
        raise HTTPException(status_code=400, detail="A Customer with this email already exists.")

    existing_customer = db.query(Customer).filter(Customer.phone_number == customer.phone_number).first()
    if existing_customer:
        raise HTTPException(status_code=400, detail="Customer with this phone number already exists.")
    
    
    db_customer = create_customerwithuser(db, customer)
    
    return db_customer



@router.post("/customers/")
def create_customer_with_room_and_hotel(customer_data: CustomerCreateRoomHobby, db: Session = Depends(get_db)):
    # Get or create hotel
    hotel = crud.get_or_create_hotel(db, customer_data.hotel)
    # Create room associated with the hotel
    room = crud.create_room(db, customer_data.room, hotel.id)
    # Create customer associated with the room
    customer = crud.create_customer2(db, customer_data, room.id)

    return {
        "message": "Customer, Room, and Hotel created successfully!",
        "customer": customer,
        "room": room,
        "hotel": hotel
    }





# @router.get("/customers/{customer_id}")
# def get_customer_details(customer_id: int, db: Session = Depends(get_db)):
#     customer = get_customer_with_room_and_hotel(db, customer_id)
#     return customer


# @router.get("/{customer_id}", response_model=CustomerCreate)
# def get_customer(customer_id: int, db: Session = Depends(get_db)):
#     customer = db.query(Customer).filter(Customer.id == customer_id).first()
#     if not customer:
#         raise HTTPException(status_code=404, detail="Customer not found")
#     return customer

@router.get("/{phone_number}", response_model=CustomerResponse)
def get_customer(phone_number: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.put("/{phone_number}", response_model=CustomerResponse)
def update_customer(phone_number: str, customer: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.phone_number == phone_number).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found.")
    
    for key, value in customer.dict(exclude_unset=True).items():
        setattr(db_customer, key, value)
    
    db.commit()
    db.refresh(db_customer)
    
    return db_customer


@router.delete("/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return {"detail": "Customer deleted"}
