from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.users import UserOut 
from ..auth.dependencies import get_current_user
from ..database import get_db

router = APIRouter()

@router.get("/me", response_model=UserOut)
def read_users_me(current_user: UserOut = Depends(get_current_user)):
    return current_user
