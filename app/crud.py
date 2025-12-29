from sqlmodel import Session, select
from .models import User
from .schemas import UserCreate
from .auth import get_password_hash

def create_user(session: Session, user_in: UserCreate):
    raw_password = user_in.password
    print(raw_password)
    hashed_pwd = get_password_hash(raw_password)
    db_user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_pwd
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_all_users(session: Session):
    return session.exec(select(User)).all()