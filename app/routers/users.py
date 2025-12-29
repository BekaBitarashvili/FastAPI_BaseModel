from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_session
from ..schemas import UserCreate, UserRead
from .. import crud

router = APIRouter()

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    return crud.create_user(session, user)

@router.get("/", response_model=list[UserRead])
def read_users(session: Session = Depends(get_session)):
    return crud.get_all_users(session)