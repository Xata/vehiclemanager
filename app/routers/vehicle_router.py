"""Defines the APIRouter for Vehicle
"""

# Import Python Dependencies
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import database
from schemas import vehicle_schema
from crud import vehicle_crud

router = APIRouter()

@router.post("/clients/{client_id}/vehicles", response_model=vehicle_schema.Vehicle, tags=["vehicles"])
def create_vehicle_for_client(client_id: str, vehicle: vehicle_schema.VehicleCreate, database: Session = Depends(database.get_database)):
    return vehicle_crud.create_new_client_vehicle(database=database, vehicle=vehicle, client_id=client_id)

@router.get("/vehicles/", response_model=list[vehicle_schema.Vehicle], tags=["vehicles"])
async def read_vehicles(start: int = 0, limit: int = 32, database: Session = Depends(database.get_database)):
    vehicles = vehicle_crud.get_vehicles(database, start=start, limit=limit)
    return vehicles

@router.delete("/vehicles/{vehicle_id}", response_model=vehicle_schema.Vehicle, tags=["vehicles"])
def delete_vehicle(vehicle_id: str, database: Session = Depends(database.get_database)):
    vehicle_to_delete = vehicle_crud.delete_vehicle(database, vehicle_id=vehicle_id)

    if not vehicle_to_delete:
        raise HTTPException(status_code=404, detail="Vehicle cannot be deleted")
    return vehicle_to_delete
