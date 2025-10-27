<h1 align="center">VehicleManager 🚚🚗🛵</h1>

<p align="center">
    <img src="https://img.shields.io/github/repo-size/Xata/vehiclemanager?style=plastic" />
    <img src="https://img.shields.io/github/languages/count/Xata/vehiclemanager?style=plastic">
    <img src="https://img.shields.io/github/languages/top/Xata/vehiclemanager?style=plastic">
    <img src="https://img.shields.io/github/last-commit/Xata/vehiclemanager?style=plastic" />
    <img src="https://img.shields.io/github/license/Xata/vehiclemanager?style=plastic" />
</p>

<p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=plastic&logo=python&logoColor=ffdd54" />
    <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=plastic&logo=html5&logoColor=white" />
    <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=plastic&logo=javascript&logoColor=%23F7DF1E" />
    <img src="https://img.shields.io/badge/FastAPI-005571?style=plastic&logo=fastapi" />
    <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=plastic&logo=sqlite&logoColor=white" />
    <img src="https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=plastic&logo=bootstrap&logoColor=white" />    
</p>

## Description

🌐 A Web App to keep track of vehicle's in your social circle.

💻 VehicleManager was created to demonstrate my programming abilities.

📷 Below is a screenshot of VehicleManager's frontend with example data:

<img src="./docs/img/vehiclemanager_frontend_screenshot.jpeg" width=100% height=100%>

## Table of Contents
- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Project Overview](#project-overview)
    - [Goals](#goals)
    - [Known Issues](#known-issues)
    - [Feature Wishlist](#feature-wishlist)
- [Getting Started](#getting-started)
    - [Project Setup](#project-setup)
    - [App Usage](#app-usage)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview

### Goals

📦 The goal of this project was to create a working web app with Python. I want to demonstrate my programming abilities and how they evolve gradually.

👨‍🎓 As my skills progress, I want to update this app to reflect those changes.

💪 I'm proud of what I have created so far and want to build off of this.

### Known Issues

The following is a list of issues that I know of:
- [ ] Deleting a client without deleting the vehicle leaves undeletable vehicle in the database 
- [ ] Error handling needs to be implemented
- [ ] Need to leverage templates so the client doesn't execute so much JavaScript code

### Feature Wishlist

This is what I plan on implementing in the near future:
- [ ] Add unit tests
- [ ] Error Handling
- [ ] Input Validation
- [x] Deployable Docker container 🐳
- [ ] Login Page and user authentication
- [ ] HTTPS instead of HTTP
- [ ] Add part lists and repair tickets to track repairs on the vehicles
- [ ] Implement dependency security for the project

## Getting Started

📌 Below you'll find the steps needed to take to setup the project and how to use it.

⚠️ Take note of any caution symbols you see! Some features haven't been implemented yet.

### Project Setup

📌 Make sure you have a modern browser, Python, and Visual Studio Code installed.

* Originally was developed with ```Python 3.10.7```. Now works with ```Python 3.13.2```

📌 Before running VehicleManager, we need to follow these steps:

1. Download the repository:
    ```
    git clone https://github.com/Xata/vehiclemanager.git
    ```

2. Setup the Python virtual environment in a new terminal window:
    * ![Windows](https://img.shields.io/badge/Windows-0078D6?style=plastic&logo=windows&logoColor=white)
        ```powershell
        python -m venv venv
        ```

3. Activate the Python virtual environment:
    * ![Windows](https://img.shields.io/badge/Windows-0078D6?style=plastic&logo=windows&logoColor=white)
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    * ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=plastic&logo=ubuntu&logoColor=white)
        ```bash
        source venv/bin/activate
        ```
    * ![macOS](https://img.shields.io/badge/macOS-%23000000.svg?style=plastic&logo=apple&logoColor=white)
        ```zsh
        source venv/bin/activate
        ```

### App Usage

📌 To run VehicleManager follow these steps:

1. Run the following commands:

    ```zsh
    docker build -t vehiclemanager .
    docker run -p 8000:8000 -v $(pwd)/data:/app/data vehiclemanager
    ```

2. In your browser, navigate to:
    - http://127.0.0.1:8000/
    - ⚠️ If this is your first time running the app, there won't be any data to display.

📌 How to use VehicleManager:

- Create a new client:
    - ⚠️ Clients cannot have the same phone number or email address
    - ⚠️ A UUID is generated in the background to identify the client
    1. Click the icon in the top right corner
    2. Enter the data to create a new client!

<img src="./docs/img/vehiclemanager_create_client.jpeg" width=100% height=100%>

- Edit a client:
    - ⚠️ The current client data is automatically put in the fields
    - ⚠️ Every field needs to have something in it for the backend to accept it
    1. Click the yellow button on the row of the client you want to edit
    2. Press submit when edits are done!

<img src="./docs/img/vehiclemanager_edit_client.jpeg" width=100% height=100%>

- Delete a client:
    - ⚠️ WARNING: The client CANNOT have any vehicles attached to them first!!
    1. Click the red button on the row of the client you want to remove
    2. Press confirm and you'll have deleted the client!

- Create a new vehicle:
    - ⚠️ You cannot change the owner field
    - ⚠️ Mileage is not displayed on the table
    1. Click on the plus button on the row of the client
    2. This will toggle the modal and now you can enter the values
    3. Press submit to create the vehicle!

<img src="./docs/img/vehiclemanager_create_vehicle.jpeg" width=100% height=100%>

- Delete a vehicle:
    - ⚠️ WARNING: You must delete all of the vehicles attached to a client before removing that client!!
    1. Click on the red button on the row of the vehicle you want to remove
    2. Press confirm to delete the vehicle!

<img src="./docs/img/vehiclemanager_delete_vehicle.jpeg" width=100% height=100%>

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

Inspiration, code snippets, etc.
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)
* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)
* [Mozilla MDN Web Docs on FetchAPI](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
* [JSDoc on how to document JavaScript Code](https://jsdoc.app/)
