from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth.dependencies import role_required
from app.models.users import User
from ..auth.jwt_handler import create_access_token
from app.crud.users import create_user, authenticate_user
from app.schemas.users import CreateSystemUser, UserCreate
from ..schemas.auth import Token
from ..database import get_db

router = APIRouter()

@router.post("/register", response_model=Token)
def register(user1: CreateSystemUser, db: Session = Depends(get_db),current_role: str = Depends(role_required(["admin"]))):
    existing_User = db.query(User).filter(User.email == user1.email).first()
    if existing_User:
        raise HTTPException(status_code=400, detail="User with this Email already exists.")    

    db_user = create_user(db, user1)
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email ,"role":user.role})
    return {"access_token": access_token, "token_type": "bearer"}


