import uuid
from fastapi import HTTPException, Depends, status, APIRouter
from sqlalchemy.exc import IntegrityError
from app.database.models import User, FilePath
from app.request.dto import UserCreate, UserBase, UserUpdate, FilePathCreate
from sqlalchemy import select
from app.database.database import get_db_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/")
async def read_users(db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User))
    db_users = result.scalars().all()
    if db_users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_users


@router.get("/{user_id}", response_model=UserBase)
async def read_user(user_id: uuid.UUID, db: AsyncSession = Depends(get_db_session)):
    db_user = await db.get(User, user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db_session)):
    try:
        db_user = User(**user.dict())
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return {"message": "User Created!", "data": db_user}
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with this username or email already exists")


@router.put("/{user_id}")
async def update_user(user_id: uuid.UUID, user: UserUpdate, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    try:
        db_user.username = user.username
        db_user.email = user.email
        await db.commit()
        await db.refresh(db_user)
        return {"message": "User Updated!", "data": db_user}
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with this username or email already exists")


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: uuid.UUID, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()

    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    await db.delete(db_user)
    await db.commit()
    return None


#
@router.post("/{user_id}/file-paths/", status_code=status.HTTP_201_CREATED)
async def create_file_path_for_user(user_id: uuid.UUID, file_path: FilePathCreate,
                                    db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    try:
        db_file_path = FilePath(**file_path.dict(), user_id=str(user_id))
        db.add(db_file_path)
        await db.commit()
        await db.refresh(db_file_path)
        return {"message": "File Path Created!", "data": db_file_path}
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Filepath for the user already exists")


@router.get("/{user_id}/file-paths/")
async def get_file_paths_for_user(user_id: uuid.UUID, retrieval_option: str = "relative",
                                  db: AsyncSession = Depends(get_db_session)):
    if retrieval_option == "relative":
        result = await db.execute(select(FilePath).filter(FilePath.user_id == str(user_id)))
        return result.scalars().all()
    elif retrieval_option == "absolute_public_url":
        # This may involve fetching and transforming data from GCP storage service
        pass
    else:
        raise HTTPException(status_code=400,
                            detail="Invalid retrieval option. Valid options: 'relative', 'absolute_public_url'")
