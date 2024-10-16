# FastAPI Project

## Overview

This project is built using **FastAPI**, a modern and high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. The project is structured to manage routes, database connections, models, and utility functions. 

## Project Structure

Here's a brief overview of the folder and file structure:
------------------------

    FASTAPI/
    ├── app/
    │   ├── routes/                  # Directory for API routes
    │   │   ├── org_api.py           # API routes for organization management   
    │   │   └── user_api.py          # API routes for user management
    │   ├── database.py              # Database connection setup
    │   ├── main.py                  # Entry point for the FastAPI application
    │   ├── models.py                # Database models
    │   ├── schemas.py               # Pydantic schemas for data validation
    │   └── utils.py                 # Utility functions
    ├── data.db                      # SQLite database file
    ├── Dockerfile                   # Docker configuration for containerizing the app
    ├── requirements.txt             # List of dependencies
    └── run.py                       # Script to run the FastAPI app

## Key Components

- **`app/routes/org_api.py`**: Contains the API routes related to managing organizations (e.g., creating, updating, deleting organizations).

- **`app/routes/user_api.py`**: Contains the API routes related to managing users (e.g., user creation, login, updating user details).

- **`app/database.py`**: Defines the database connection. In this case, the project is likely using SQLite (`data.db`).

- **`app/models.py`**: Contains SQLAlchemy models that map to the database tables.

- **`app/schemas.py`**: Defines the Pydantic models used for request and response validation.

- **`app/utils.py`**: Contains utility functions that are used throughout the project.

- **`main.py`**: This file includes the FastAPI app instance and registers the routes defined in the `org_api.py` and `user_api.py`.

- **`Dockerfile`**: Used to containerize the application, enabling it to be deployed in a consistent environment.

- **`requirements.txt`**: A file containing the project dependencies, which can be installed using:
  
  ```bash
  pip install -r requirements.txt

  uvicorn app.main:app --reload

## How to Run the Project

### Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.7+**
- **FastAPI** and its dependencies (listed in `requirements.txt`)
- **Uvicorn** (the ASGI server)
- **SQLite** (included as `data.db`)

### Steps to Run Locally

1. **Clone the repository**: To get started, clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   Install the dependencies: Navigate to the project directory.  
2. **Using pip**: Install the required dependencies listed in requirements.txt
    ```bash
    pip install -r requirements.txt
3. **Run the FastAPI application**: Once the dependencies are installed, you can start the FastAPI application by running:

    ```bash
    python run.py
4. **Access the API**: Open your browser and go to:
    ```bash
    http://127.0.0.1:8000
You can also explore the API documentation automatically provided by FastAPI at:
    http://127.0.0.1:8000/docs.

Alternatively, you can view the API using the ReDoc interface: http://127.0.0.1:8000/redoc

## Running with Docker

If you prefer to run the application in a Docker container, follow these steps:

1. **Build the Docker image**: To build the Docker image for the application, navigate to the project directory and run:
   ```bash
   docker build -t fastapi-app .

2. **Run the Docker container**: After building the image, you can run the container with the following command:
    ```bash
    docker run -d -p 8000:8000 fastapi-app.

3. **Access the API**: The application will now be running in the Docker container, and you can access it through your browser at:
    ```bash
    http://127.0.0.1:8000

## API Documentation
FastAPI automatically generates interactive API documentation. Once the project is running, you can explore the API endpoints and test them directly from your browser using Swagger UI. 

**The documentation can be accessed at**:

    http://127.0.0.1:8000/docs

In addition to Swagger UI, FastAPI also provides another documentation interface using ReDoc. You can view the ReDoc API documentation at:

    http://127.0.0.1:8000/redoc
    
