# Hacker news fastapi application

## Prerequisites

Install docker on your system

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)


1. **Clone the Repository**

   ```sh
   https://github.com/Jagadisg/Top-10-stories

2. **Build the Docker images.**

    ```sh
    docker compose up --build

3. **Access the Application**

    **Once the containers are up and running, you can access the backend and frontend in your web browser :**

    ```sh
    http://localhost:5000 to access frontend 
    http://127.0.0.1:8000/api/docs to access fastapi backend 

4. **Test api using swagger by accessing docs,redoc endpoint which is easier than postman and pytest will run by docker build itself**

    ```sh
    http://127.0.0.1:8000/api/docs
    or by accessing 
    http://localhost:5000
