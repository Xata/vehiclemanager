"""Defines the APIRouter for Client
"""

# Import Python Dependencies
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import database
from schemas import client_schema
from crud import client_crud

router = APIRouter()

@router.post("/clients/", response_model=client_schema.Client, tags=["clients"])
def create_client(client: client_schema.ClientCreate, database: Session = Depends(database.get_database)):
    # Check to see if the client already exists
    database_client = client_crud.get_client_by_phone(database, client_phone=client.client_phone)

    if database_client:
        raise HTTPException(status_code=400, detail="This phone number is already registered")
    
    # Create the new client
    return client_crud.create_client(database, client)

@router.get("/clients/", response_model=list[client_schema.Client], tags=["clients"])
def read_clients(start: int = 0, limit: int = 100, database: Session = Depends(database.get_database)):
    clients = client_crud.get_clients(database, start=start, limit=limit)
    return clients

@router.get("/clients/{client_id}", response_model=client_schema.Client, tags=["clients"])
def read_client_by_id(client_id: str, database: Session = Depends(database.get_database)):
    client = client_crud.get_client(database=database, client_id=client_id)
    return client

@router.delete("/clients/{client_id}", response_model=client_schema.Client, tags=["clients"])
def delete_client(client_id: str, database: Session = Depends(database.get_database)):
    client_to_delete = client_crud.delete_client(database, client_id=client_id)
    if not client_to_delete:
        raise HTTPException(status_code=404, detail="Client cannot be deleted")
    return client_to_delete

@router.patch("/clients/{client_id}", response_model=client_schema.Client, tags=["clients"])
def update_client(client_id: str, update_client: client_schema.ClientBase, database: Session = Depends(database.get_database)):
    database_client = client_crud.get_client(database=database, client_id=client_id)
    
    if database_client is None:
        raise HTTPException(status_code=404, detail="Client cannot be updated")
    
    client_crud.update_client(database=database, client=database_client, updates=update_client)

    return client_crud.get_client(database=database, client_id=client_id)
