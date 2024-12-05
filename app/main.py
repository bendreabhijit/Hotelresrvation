from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from app.database import engine, Base
from app.routers import hotel_router, room_router, customer_router,reservation_router,auth, users
from fastapi.middleware.cors import CORSMiddleware

# Initialize database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify the allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

app.include_router(auth.router)
# Include routers
app.include_router(hotel_router, prefix="/hotels", tags=["hotels"])    # he routers
app.include_router(room_router, prefix="/rooms", tags=["rooms"])
app.include_router(customer_router, prefix="/customers", tags=["customers"])
app.include_router(reservation_router, prefix="/reservations", tags=["reservations"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
