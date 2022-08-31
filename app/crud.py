""" Contains all of the CRUD functions of the app
"""

# Import Modules
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from uuid import uuid4

import models
import schemas


def get_client(database: Session, client_id: str):
    """
    Used to pull a client from the database based on their client_id
    """
    return database.query(models.Client).filter(models.Client.client_id == client_id).first()


def get_client_by_email(database: Session, client_email: str):
    """
    Used to pull a client from the database based on their email
    """
    return database.query(models.Client).filter(models.Client.client_email == client_email).first()


def get_client_by_phone(database: Session, client_phone: int):
    """
    Used to pull a client from the databased based on their phone number
    """
    return database.query(models.Client).filter(models.Client.client_phone == client_phone).first()


def get_clients(database: Session, skip: int = 0, limit: int = 100):
    """
    Used to pull all the clients from the database
    """
    return database.query(models.Client).offset(skip).limit(limit).all()


def create_client(database: Session, client: schemas.ClientCreate):
    """
    Used to create a new client. Generates a new uuid for the new client
    """

    # Generate a unique id for the new client
    new_client_id = str(uuid4())

    # Create a new client
    database_new_client = models.Client(client_id=new_client_id, client_name=client.client_name,
                                        client_email=client.client_email, client_phone=client.client_phone)

    # Make database changes
    database.add(database_new_client)
    database.commit()
    database.refresh(database_new_client)

    # Return the new client
    return database_new_client

def update_client(database: Session, client: models.Client, updates: schemas.ClientBase):
    """
    Used to update a client's attributes. It cannot modify the client's client_id
    """
    update_data = updates.dict(exclude_unset=True)

    # Parse through update_data for the changes
    for key, value in update_data.items():
        # Set the new attributes
        setattr(client, key, value)
    
    # Commit to the database
    database.commit()

def delete_client(database: Session, client_id: str):
    """
    Used to delete a client from the database. Deletes the first client with matching client_id
    """
    # Find the client in the database
    database_deletable_client = get_client(database=database, client_id=client_id)
    
    # Make database changes
    if database_deletable_client:
        database.delete(database_deletable_client)
        database.commit()

        # Debug Print Commands
        print("Successfully deleted from the database")

    # Return the deleted client
    return database_deletable_client

def get_vehicles(database: Session, skip: int = 0, limit: int = 100):
    """
    Used to get all of the vehicles in the database
    """

    return database.query(models.Vehicle).offset(skip).limit(limit).all()

def create_new_client_vehicle(database: Session, vehicle: schemas.VehicleCreate, client_id: str):
    """
    Used to create a new vehicle for a client

    new_vehicle_id: Generated using uuid4
    """

    # Generate a unique id for the new vehicle
    new_vehicle_id = str(uuid4())

    # Create a new vehicle
    database_vehicle = models.Vehicle(**vehicle.dict(), vehicle_id=new_vehicle_id, vehicle_owner_id=client_id)

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
    return database.query(models.Vehicle).filter(models.Vehicle.vehicle_id == vehicle_id).first()

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
        print("Successfully deleted {vehicle_id} from the database")

    # Return the deleted vehicle
    return database_deletable_vehicle