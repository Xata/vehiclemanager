""" Provides pydantic models/schema for FastAPI
"""

# Import Modules
from pydantic import BaseModel, Field


class VehicleBase(BaseModel):
    """
    VehicleBase is where all of the attributes for the Vehicle schema are defined. Except the vehicle_id.
    """

    # Define the VehicleBase Schema
    vehicle_year: int | None = Field(default=None, example="2020")
    vehicle_make: str | None = Field(default=None, example="Toyota")
    vehicle_model: str | None = Field(default=None, example="Corolla")
    vehicle_mileage: int | None = Field(default=None, example="78921")


class VehicleCreate(VehicleBase):
    """
    VehicleCreate schema is blank for now
    """

    pass


class Vehicle(VehicleBase):
    """
    Vehicles are the what you store in the database based on the client/friend

    Attributes:
        vehicle_id: uuid stored as a string
        vehicle_owner_id: The client_id of the owner
    """

    vehicle_id: str
    vehicle_owner_id: str

    class Config:
        orm_mode = True


class ClientBase(BaseModel):
    """
    ClientBase schema
    """

    # Define the ClientBase Schema
    client_name: str | None = Field(default=None, example="Jane Doe")
    client_email: str | None = Field(
        default=None, example="jdoe@testdomain.com")
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
    client_vehicles: list[Vehicle] = []

    # Configure class to be used with an orm
    class Config:
        orm_mode = True
