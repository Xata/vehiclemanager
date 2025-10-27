# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

VehicleManager is a FastAPI web application for tracking vehicle information and repairs for clients in your social circle. It uses SQLAlchemy ORM with SQLite for data persistence and serves a single-page application frontend.

## Running the Application

**Setup virtual environment (first time only):**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

**Run the development server:**
```bash
python app/main.py
```

The app will be available at http://127.0.0.1:8000/

**Activate virtual environment (if not already active):**
```bash
source venv/bin/activate  # On macOS/Linux
.\venv\Scripts\Activate.ps1  # On Windows
```

## Architecture

### Application Structure

The application follows a modular FastAPI architecture with clear separation of concerns:

- **app/main.py** - Application entry point, FastAPI app initialization, middleware configuration, and router inclusion
- **app/routers/** - API route handlers (client_router.py, vehicle_router.py)
- **app/models/** - SQLAlchemy ORM models (client_model.py, vehicle_model.py)
- **app/schemas/** - Pydantic schemas for request/response validation (client_schema.py, vehicle_schema.py)
- **app/crud/** - Database operations (client_crud.py, vehicle_crud.py)
- **app/database/database.py** - SQLAlchemy engine, session management, and base class
- **app/settings.py** - Application settings using Pydantic BaseSettings
- **app/templates/** - Jinja2 HTML templates (index.html)
- **app/static/** - Static assets (JavaScript, images)

### Database Schema

The application uses SQLite with two main tables:

**Clients table:**
- client_id (String, Primary Key) - UUID generated via uuid4()
- client_name (String)
- client_email (String)
- client_phone (Integer) - stored without dashes

**Vehicles table:**
- vehicle_id (String, Primary Key) - UUID generated via uuid4()
- vehicle_year (Integer)
- vehicle_make (String, max 32 chars)
- vehicle_model (String, max 64 chars)
- vehicle_mileage (Integer)
- vehicle_owner_id (String, Foreign Key to clients.client_id)

**Important relationship:** Client has a one-to-many relationship with Vehicle through the `client_vehicles` relationship. A client cannot be deleted if they have vehicles attached.

### Data Flow Pattern

The application follows this consistent pattern for all operations:

1. **Router** (app/routers/) receives HTTP request
2. **Router** validates input using **Pydantic schemas** (app/schemas/)
3. **Router** calls **CRUD function** (app/crud/) with database session
4. **CRUD function** performs database operations using **SQLAlchemy models** (app/models/)
5. **Router** returns response serialized through **Pydantic schemas**

### Key Implementation Details

- **Database initialization:** On startup, the app checks if the database exists at `sqlite:///./app/database/vehiclemanager.sqlite`. If not, it creates tables using SQLAlchemy metadata.
- **Settings management:** Uses `@lru_cache()` to ensure only one Settings instance is created.
- **UUID generation:** All entity IDs are UUIDs converted to strings using Python's uuid4().
- **CORS:** Configured to allow all origins (app/main.py:53).

## Known Issues

From the README, be aware of these existing issues when making changes:

- Deleting a client without first deleting their vehicles leaves undeletable vehicles in the database
- Error handling is minimal and needs improvement
- Frontend executes significant JavaScript; the project aims to leverage server-side templates more

## Development Notes

- Originally developed with Python 3.10.7
- **Pydantic V2:** The codebase has been updated to work with Pydantic V2 (2.12.3):
  - Uses `pydantic-settings` package for `BaseSettings` (instead of `pydantic.BaseSettings`)
  - Schema Config uses `from_attributes = True` (instead of `orm_mode = True`)
  - All Settings class attributes require type annotations
- Database path is hardcoded in multiple locations (app/database/database.py and app/main.py)
- The application uses relative imports throughout (e.g., `from database import database`)
- Static files and templates use relative paths from the app root
- There's a deprecation warning about `on_event` - FastAPI recommends using lifespan event handlers instead
