from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, index=True, nullable=False, unique=True,
                default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    file_paths = relationship("FilePath", back_populates="user")


class FilePath(Base):
    __tablename__ = "file_paths"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String, unique=True)
    user_id = Column(String, ForeignKey("users.id"))

    user = relationship("User", back_populates="file_paths")
