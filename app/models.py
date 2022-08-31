""" Provides classes for SQLAlchemy models.
"""

# Import Modules
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Client(Base):
    """
    Client class is for creating a SQLAlchemy model of a Client

    The client_id is the primary key. Its a uuid stored as a string. The tablename is defined as clients

    Attributes:
        client_id: The primary key of the client. A uuid stored as a string
        client_name: Full name. Seperated by a space. Stored as a string
        client_email: Email. Stored as a string
        client_phone: Phone number. Stored as an integer with no dashes
    """
    __tablename__ = "clients"

    # Define the Client class's columns in the table
    client_id = Column(String, primary_key=True, index=True)
    client_name = Column(String)
    client_email = Column(String)
    client_phone = Column(Integer)

    client_vehicles = relationship("Vehicle", back_populates="vehicle_owner")


class Vehicle(Base):
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
