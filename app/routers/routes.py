from fastapi import HTTPException, Depends, status, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database.database import engine
from app.database.models import User, Base, FilePath
from app.request.dto import UserCreate, UserUpdate, UserBase, FilePathCreate
from app.database.database import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/")
async def read_users(db: Session = Depends(get_db)):
    db_user = db.query(User).all()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@router.get("/{user_id}", response_model=UserBase)
async def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User(username=user.username, email=user.email)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"message": "User Created!", "data": db_user}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with this username or email already exists")


@router.put("/{user_id}")
async def update_user(user_id: str, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    try:
        db_user.username = user.username
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
        return {"message": "User Updated!", "data": db_user}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="User with this username or email already exists")


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    db.delete(db_user)
    db.commit()
    return None


@router.post("/{user_id}/file-paths/", status_code=status.HTTP_201_CREATED)
async def create_file_path_for_user(user_id: str, file_path: FilePathCreate, db: Session = Depends(get_db)):
    print(f"file_path : {file_path.dict()}")
    try:
        db_file_path = FilePath(**file_path.dict(), user_id=user_id)
        db.add(db_file_path)
        db.commit()
        db.refresh(db_file_path)
        return {"message": "File Path Created!", "data": db_file_path}
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Filepath for the user already exists")


@router.get("/{user_id}/file-paths/")
def get_file_paths_for_user(user_id: str, retrieval_option: str = "relative", db: Session = Depends(get_db)):
    if retrieval_option == "relative":
        return db.query(FilePath).filter(FilePath.user_id == user_id).all()
    elif retrieval_option == "absolute_public_url":
        # This may involve fetching and transforming data from GCP storage service
        pass
    else:
        raise HTTPException(status_code=400,
                            detail="Invalid retrieval option. Valid options: 'relative', 'absolute_public_url'")
