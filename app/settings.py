"""Contains default settings for VehicleManager
"""

# Import Python Dependencies
from pydantic_settings import BaseSettings

from database import database


class Settings(BaseSettings):
    """
    Contains all the default settings used for a VehicleManager instance
    """
    app_name: str = "VehicleManager"
    app_description: str = "Vehicle Manager helps you track what repairs you've done to your friends' vehicles!"
    app_version: str = "0.0.1"
    app_host: str = "127.0.0.1"
    app_port: int = 8000
    app_templates_directory: str = "./app/templates"
    app_static_files_directory: str = "./app/static"
    app_database_path: str = database.DATABASE_PATH