# Import CRUD operations for each model
# In app/crud/__init__.py

from .hotel import create_hotel, get_hotel, update_hotel, delete_hotel,get_hotelbylocation
from .room import create_room, get_room, update_room, delete_room, get_room_by_id
from .customer import create_customerwithuser, get_customer, update_customer, delete_customer
# from .reservation import create_reservation, get_reservation, update_reservation, delete_reservation
from app import models
from .users import create_user, get_user_by_username, authenticate_user
 
from app.models import User
