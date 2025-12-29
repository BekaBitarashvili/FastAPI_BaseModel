from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str
    email: str
    password: str = Field(..., max_length=72)

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr