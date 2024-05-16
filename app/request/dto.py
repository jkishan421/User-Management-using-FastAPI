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


class FilePathBase(BaseModel):
    path: str


class FilePathCreate(FilePathBase):
    pass


class FilePathDto(FilePathBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True
