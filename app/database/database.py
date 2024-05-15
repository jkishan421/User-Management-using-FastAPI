from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define SQLAlchemy database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
