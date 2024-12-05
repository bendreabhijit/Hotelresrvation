from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate
 
from passlib.context import CryptContext

from app.schemas.users import CreateSystemUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashed_password(password :str):     
    return pwd_context.hash(password)

def get_user_by_username(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: CreateSystemUser):
    Userhashed_password=hashed_password(user.password)
    db_user = User(email=user.email,password=Userhashed_password,role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_username(db, email)
    if not user or not pwd_context.verify(password, user.password):
        return False
    return user
