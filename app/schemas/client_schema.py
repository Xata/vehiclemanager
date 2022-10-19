"""Provides the Client schema for FastAPI
"""

# Import Python Dependencies
from pydantic import BaseModel, Field

from schemas import vehicle_schema

class ClientBase(BaseModel):
    """
    ClientBase schema
    """

    # Define the ClientBase Schema
    client_name: str | None = Field(default=None, example="Jane Doe")
    client_email: str | None = Field(default=None, example="jdoe@example.com")
    
    # Example phone number is the US Naval Observatory Master Clock Line
    client_phone: int | None = Field(default=None, example="2027621401")


class ClientCreate(ClientBase):
    """
    ClientCreate schema is blank for now
    """

    pass


class Client(ClientBase):
    """
    Clients are your friends, family, or clients that brought their vehicle to you to look at
    Attributes:
        client_id: uuid stored as a string
        client_vehicles: The list of vehicles this client/friend owns
    """
    # Define the Client Schema
    client_id: str
    client_vehicles: list[vehicle_schema.Vehicle] = []

    # Configure class to be used with an orm
    class Config:
        orm_mode = True