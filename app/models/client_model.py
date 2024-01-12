"""Defines the Client Model
"""

# Import Python Dependencies
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import database

class Client(database.Base):
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