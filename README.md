# Django REST Framework Backend Application

This is a backend application built using Django and Django REST Framework (DRF). The application connects to a MySQL database and includes two basic views to demonstrate the functionality.

## Features

- Two basic API views built using Django REST Framework
- Connected to a MySQL database
- Simple backend setup for handling requests and responses

## Installation

### Prerequisites

- Python 3.x
- MySQL database

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/abhishek173/Project-Backend.git
    cd Project-Backend
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:

    - Create a MySQL database and user.
    - Update the `DATABASES` configuration in the `settings.py` file with your MySQL credentials.

    Example:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. Run migrations to set up the database:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. The Backend is now running at `http://127.0.0.1:8000/`.

## Usage

You can interact with the API using tools like Postman or cURL.

- `GET /api/projects/`: Retrieves Projects.
- `POST /api/login/`: For User Login.


