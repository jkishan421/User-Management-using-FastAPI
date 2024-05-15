from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


# Pydantic model for creating a new user
class UserCreate(UserBase):
    pass


# Pydantic model for updating a user
class UserUpdate(UserBase):
    pass
