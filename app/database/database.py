""" Contains code to initialize SQLAlchemy
"""

# Import Modules
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define global variables
DATABASE_NAME = "vehiclemanager.sqlite"
# Use environment variable if set (for Docker), otherwise use default path (for local dev)
DATABASE_PATH = os.getenv("DATABASE_PATH", f"sqlite:///./app/database/{DATABASE_NAME}")
# Extract actual file path from SQLite URL for file operations
# SQLite URL format: sqlite:///path or sqlite:////absolute/path
DATABASE_FILE_PATH = DATABASE_PATH.replace("sqlite:///", "").lstrip("/")
if DATABASE_PATH.startswith("sqlite:////"):
    # Absolute path (4 slashes)
    DATABASE_FILE_PATH = "/" + DATABASE_PATH.replace("sqlite:////", "")
#SQLALCHEMY_DATABASE_PATH = "sqlite:///./data/vehicle_data.db"

# Create a SQLAlchemy engine to interact with the database
database_engine = create_engine(
    DATABASE_PATH, connect_args={"check_same_thread": False}
)

# Create an instance of a database session
LocalDatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=database_engine)

# Get database connection
def get_database():
    database = LocalDatabaseSession()
    try:
        yield database
    finally:
        database.close()

# Create a Base class that will be used to create the ORM models
Base = declarative_base()