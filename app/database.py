""" Contains code to initialize SQLAlchemy
"""

# Import Modules
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define global variables
SQLALCHEMY_DATABASE_PATH = "sqlite:///./data/vehicle_data.db"

# Create a SQLAlchemy engine to interact with the database
sqlalchemy_engine = create_engine(
    SQLALCHEMY_DATABASE_PATH, connect_args={"check_same_thread": False}
)

# Create an instance of a database session
LocalDatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=sqlalchemy_engine)

# Create a Base class that will be used to create the ORM models
Base = declarative_base()
