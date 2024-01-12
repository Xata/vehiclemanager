"""Contains code to run Vehicle Manager
"""

# Import Python Dependencies
import uvicorn
import os

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from functools import lru_cache

from routers import client_router, vehicle_router
from database import database
from settings import Settings

# Declare App Variables
APP_TITLE = "Vehicle Manager"
APP_DESCRIPTION = "Vehicle Manager helps you track what repairs you've done to your friends' vehicles!"
APP_VERSION = "0.0.1"
APP_HOST = "127.0.0.1"
APP_PORT = 8000
APP_TEMPLATES_DIRECTORY = "./app/templates"
APP_STATIC_FILES_DIRECTORY = "./app/static"
APP_DATABASE_PATH = database.DATABASE_PATH

# Define FastAPI parameters
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

# Get default settings
@lru_cache()
def get_default_settings():
    """Returns default app settings

    lru_cache allows for only one instance to be created of a settings object

    """
    return Settings()

# Create Jinja2 Templates
templates = Jinja2Templates(directory=APP_TEMPLATES_DIRECTORY)

# Mount the static files directory
app.mount("/static", StaticFiles(directory=APP_STATIC_FILES_DIRECTORY), name="static")

# Add Middleware to app
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_headers=["*"], expose_headers=["*"],)

# Include submodule Routers
app.include_router(client_router.router)
app.include_router(vehicle_router.router)

@app.on_event("startup")
def startup_check_database():
    # Create new database is it doesn't exist
    if not os.path.exists(APP_DATABASE_PATH):
        database.Base.metadata.create_all(bind=database.database_engine)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/info")
def info(settings: Settings = Depends(get_default_settings)):
    return {
        "app_name": settings.app_name,
        "app_description": settings.app_description,
        "app_version": settings.app_version,
        "app_host": settings.app_host,
        "app_port": settings.app_port,
    }

# Run Vehicle Manager on uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host=APP_HOST, port=APP_PORT)