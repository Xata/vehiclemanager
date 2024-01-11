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
    <img src="https://img.shields.io/badge/Flask-000000?style=plastic&logo=flask" />
    <img src="https://img.shields.io/badge/sqlite-%2307405e.svg?style=plastic&logo=sqlite&logoColor=white" />
</p>

## Description

🌐 A Web App to keep track of vehicle's in your social circle.

💻 VehicleManager was created to demonstrate my programming abilities.

## Table of Contents
- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Project Overview](#project-overview)
    - [Goals](#goals)
    - [Feature Wishlist](#feature-wishlist)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview

### Goals

📦 The goal of this project was to create a working web app with Python.

👨‍🎓 As my skills progress, I want to update this app to reflect those changes.

💪 I'm proud of what I have created so far and want to build off of this.

### Feature Wishlist

This is what I plan on implementing in the near future:
- [ ] Add unit tests
- [ ] HTTPS instead of HTTP
- [ ] Add part lists and repair tickets to track repairs on the vehicles
- [ ] Add environment variables
- [ ] Make app production ready

## Usage

⚠️ Do not deploy in production environment.

### Running 

1. Build the Docker image:

    Open a terminal, navigate to the root of the project, and run the following command to build the Docker image:
    ```bash
   docker build -t vehiclemanager .
   ```
   
2. Run the Docker container:

    Once the image is built, you can run a container based on that image:
    ```bash
   docker run -p 5000:5000 vehiclemanager
   ```
3. Access the app:

    Navigate to http://127.0.0.1:5000 in your favorite web browser to view the app.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements

Inspiration, code snippets, etc.
* [Flask Documentation](https://flask.palletsprojects.com/)
* [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)
* [Mozilla MDN Web Docs on FetchAPI](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
* [JSDoc on how to document JavaScript Code](https://jsdoc.app/)