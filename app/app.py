""" Contains code to run Vehicle Manager

This contains all of the code required to run Vehicle Manager. At the moment, the FastAPI routes are here too. 
If you run this file as is, it'll check if the database exists and if not just create one. 
Be sure to initialize the virtual python environment and install the modules in requirements.txt

TODO: Seperate the FastAPI from the main app module
TODO: Add environment variables for the global variables section
TODO: Add dev environment code like automating database creation
TODO: Create unit tests

"""

# Import Modules
import uvicorn
import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import LocalDatabaseSession, sqlalchemy_engine


# Declare Global Variables
APP_TITLE = "Vehicle Manager"
APP_DESCRIPTION = "Vehicle Manager helps you track what repairs you've done to your friends' vehicles!"
APP_VERSION = "0.0.1"
DATABASE_PATH = "./data/vehicle_data.db"

# Create a database. This is for debugging and starting the project
if not os.path.exists(DATABASE_PATH):
    print(DATABASE_PATH)
    models.Base.metadata.create_all(bind=sqlalchemy_engine)

# Define FastAPI parameters
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

# Dependency
def get_database():
    database = LocalDatabaseSession()
    try:
        yield database
    finally:
        database.close()

@app.get("/")
def root():
    return {"message": "Hello!!"}

@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, database: Session = Depends(get_database)):
    # Check to see if the client already exists
    database_client = crud.get_client_by_phone(database, client_phone=client.client_phone)

    if database_client:
        raise HTTPException(status_code=400, detail="This phone number is already registered")
    
    # Create the new client
    return crud.create_client(database, client)

@app.get("/clients/", response_model=list[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, database: Session = Depends(get_database)):
    clients = crud.get_clients(database, skip=skip, limit=limit)
    return clients

@app.delete("/clients/{client_id}", response_model=schemas.Client)
def delete_client(client_id: str, database: Session = Depends(get_database)):
    client_to_delete = crud.delete_client(database, client_id=client_id)
    if not client_to_delete:
        raise HTTPException(status_code=404, detail="Client cannot be deleted")
    return client_to_delete

@app.patch("/clients/{client_id}", response_model=schemas.Client)
def update_client(client_id: str, update_client: schemas.ClientBase, database: Session = Depends(get_database)):
    database_client = crud.get_client(database=database, client_id=client_id)
    
    if database_client is None:
        raise HTTPException(status_code=404, detail="Client cannot be updated")
    
    crud.update_client(database=database, client=database_client, updates=update_client)

    return crud.get_client(database=database, client_id=client_id)

@app.post("/clients/{client_id}/vehicles", response_model=schemas.Vehicle)
def create_vehicle_for_client(client_id: str, vehicle: schemas.VehicleCreate, database: Session = Depends(get_database)):
    return crud.create_new_client_vehicle(database=database, vehicle=vehicle, client_id=client_id)

@app.get("/vehicles/", response_model=list[schemas.Vehicle])
def read_vehicles(skip: int = 0, limit: int = 100, database: Session = Depends(get_database)):
    vehicles = crud.get_vehicles(database, skip=skip, limit=limit)
    return vehicles

@app.delete("/vehicles/{vehicle_id}", response_model=schemas.Vehicle)
def delete_vehicle(vehicle_id: str, database: Session = Depends(get_database)):
    vehicle_to_delete = crud.delete_vehicle(database, vehicle_id=vehicle_id)

    if not vehicle_to_delete:
        raise HTTPException(status_code=404, detail="Vehicle cannot be deleted")
    return vehicle_to_delete

# Run app for debugging
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
