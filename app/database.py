from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database URL -> will create 'recipes.db' file
SQLALCHEMY_DATABASE_URL = "sqlite:///./recipes.db"

# Create the SQLALCHEMY "engine" -> the core interface
# 'check_same_thread' arg. is specifically needed for SQLite in FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
) 

# Create a SessionLocal class -> each instance will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class -> used for building my database models later
Base = declarative_base()