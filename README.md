# Vehicle Manager

Vehicle Manager is for keeping track of repairs done to friends' vehicles!

## Description

Vehicle Manager is a web application that I envisoned would help keep track of repairs done on personal 
vehicles and other vehicles that people have brought to me to help repair. I wanted to create something that
can be hosted locally and deployed easily. 

Vehicle Manager still has a little ways to go but it's chugging along!

## Built With

These are the technologies used (so far) to create Vehicle Manager:
- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [SQLite](https://www.sqlite.org/index.html)

## Getting Started

### Preqrequisities

Ensure that you have vscode installed.

Create a new virtual environment (you can do this in the root project folder):
> python -m venv venv

Navigate to the scripts folder and activate the virtual environment (Windows 10):
> ./Activate.ps1

Run the following command to download the packages needed (via [requirements.txt](/requirements.txt)):
> python -m pip install -r requirements.txt

### Run and Build (So far)

Run app.py for debugging the API and CRUD commands.

## Roadmap

Vehicle Manager still has a little ways to go before its working completely. 
Here you can find the project's roadmap to becomming a function application:

- Create a better development environment:
    - [ ] Create environment variables for the application
    - [ ] Containerize Vehicle Manager for easy deployments
    - [ ] Create unit tests for testing the apps functionality
    - [ ] Implement Alembic for managing the database changes during development
    - [ ] Add logging

- Finish the basic backend functionality:
    - [ ] Add users
    - [ ] Add user authentication and security

- Create a frontend:
    - [ ] Create a basic frontend website to interact with the app

- Future features:
    - [ ] Add ability to print out static cling labels for service reminders

## Licensing

The project uses the MIT License. You can find more information in [LICENSE.md](/LICENSE.md)

This project is a personal/hobby/student project that would be something I personally would use.



