# # Import each schema to make them accessible from `app.schemas`
# from .hotel import HotelBase, HotelCreate, HotelUpdate
# from .room import RoomBase, RoomCreate, RoomUpdate
# from .customer import CustomerBase, CustomerCreate, CustomerUpdate
# from .reservation import ReservationBase, ReservationCreate, ReservationUpdate
# from .hotel import HotelBase, HotelCreate, HotelUpdate, Hotel

from .hotel import  HotelCreate, HotelResponse, HotelUpdate,hotelLocationResponse
from .room import RoomCreate, RoomCreate, RoomUpdate, RoomResponse,RoomUpdateResponse
from .customer import CustomerBase, CustomerCreate, CustomerUpdate, CustomerCreateRoomHobby
from .reservation import ReservationBase, ReservationCreate, ReservationUpdate
from .users import UserCreate


 
