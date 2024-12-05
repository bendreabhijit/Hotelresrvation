# Import routers for easy access
from .hotel import router as hotel_router
from .room import router as room_router
from .customer import router as customer_router
from .reservation import router as reservation_router
from .customer import CustomerCreate, CustomerUpdate, CustomerCreateRoomHobby
from app import models
from app.schemas.users import UserOut