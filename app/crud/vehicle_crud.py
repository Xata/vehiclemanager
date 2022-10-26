"""Contains all the crud functions for Vehicles
"""

# Import Python Dependencies
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from uuid import uuid4

from models import vehicle_model
from schemas import vehicle_schema

def get_vehicles(database: Session, start: int = 0, limit: int = 32):
    """
    Used to get all of the vehicles in the database
    """

    return database.query(vehicle_model.Vehicle).offset(start).limit(limit).all()

def create_new_client_vehicle(database: Session, vehicle: vehicle_schema.VehicleCreate, client_id: str):
    """
    Used to create a new vehicle for a client
    new_vehicle_id: Generated using uuid4
    """

    # Generate a unique id for the new vehicle
    new_vehicle_id = str(uuid4())

    # Create a new vehicle
    database_vehicle = vehicle_model.Vehicle(**vehicle.dict(), vehicle_id=new_vehicle_id, vehicle_owner_id=client_id)

    # Update the database
    database.add(database_vehicle)
    database.commit()
    database.refresh(database_vehicle)

    # Return the new vehicle
    return database_vehicle

def get_vehicle(database: Session, vehicle_id: str):
    """
    Used to pull a vehicle from the database based on the vehicle_id
    """
    return database.query(vehicle_model.Vehicle).filter(vehicle_model.Vehicle.vehicle_id == vehicle_id).first()

def delete_vehicle(database: Session, vehicle_id: str):
    """
    Used to delete a vehicle from the database. Deletes the first vehicle with matching vehicle_id
    """
    # Find the vehicle in the database
    database_deletable_vehicle = get_vehicle(database=database, vehicle_id=vehicle_id)
    
    # Make database changes
    if database_deletable_vehicle:
        database.delete(database_deletable_vehicle)
        database.commit()

        # Debug Print Commands
        # print(f"Successfully deleted {vehicle_id} from the database")

    # Return the deleted vehicle
    return database_deletable_vehicle