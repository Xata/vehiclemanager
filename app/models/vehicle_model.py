"""Defines the Vehicle Model
"""

# Import Python Dependencies
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import database

class Vehicle(database.Base):
    """
    Vehicle class is for creating a SQLAlchemy model of a Vehicle
    Each vehicle has a vehicle_id which is the primary key. Its a uuid stored as a string. Each vehicle also has vehicle_owner_id which is a Foreign key used to identify the owner
    Attributes:
        vehicle_id: The primary key. A uuid stored as a string
        vehicle_year: Year. Stored as a Integer
        vehicle_make: Name of the manufacturer. Stored as a string
        vehicle_model: Model name. Stored as a string
        vehicle_mileage: Current mileage of the vehicle. Stored as an integer
    """
    __tablename__ = "vehicles"

    # Define the Vehicle class's columns in the table
    vehicle_id = Column(String, primary_key=True, index=True)
    vehicle_year = Column(Integer)
    vehicle_make = Column(String(32))
    vehicle_model = Column(String(64))
    vehicle_mileage = Column(Integer)

    vehicle_owner_id = Column(String, ForeignKey("clients.client_id"))
    vehicle_owner = relationship("Client", back_populates="client_vehicles")