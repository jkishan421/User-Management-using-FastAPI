from sqlalchemy import String, ForeignKey
import uuid
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import List
from sqlalchemy import orm


class Base(orm.DeclarativeBase):
    """Base database model."""

    id: orm.Mapped[uuid.UUID] = orm.mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    file_paths: Mapped[List["FilePath"]] = relationship("FilePath", back_populates="user")


class FilePath(Base):
    __tablename__ = "file_paths"

    path: Mapped[str] = mapped_column(String, unique=True)
    user_id: Mapped[str] = mapped_column(String, ForeignKey("users.id"))

    user: Mapped["User"] = relationship("User", back_populates="file_paths")
