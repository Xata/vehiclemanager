"""Provides the Vehicle schema for FastAPI
"""

# Import Python Dependencies
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