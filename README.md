# Portfolio Management API

This is a Django Rest Framework (DRF) project that provides a RESTful API for managing projects, skills, achievements, and contacts. It uses JWT (JSON Web Tokens) for secure authentication and PostgreSQL as the database.

## Features

- **JWT Authentication**: Secure user authentication using JSON Web Tokens.
- **CRUD Operations**: Full CRUD (Create, Read, Update, Delete) functionality for projects, skills, achievements, and contacts.
- **PostgreSQL Database**: Scalable and reliable database for storing application data.

## Requirements

- Python 3.x
- Django
- Django REST Framework
- djangorestframework-simplejwt
- PostgreSQL

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Install pipenv if not already installed:**

   ```bash
   pip install pipenv
   ```

3. **Install the dependencies:**

   ```bash
   pipenv install
   ```

4. **Activate the virtual environment:**

   ```bash
   pipenv shell
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the server:**

   ```bash
   python manage.py runserver
   ```

### Endpoints

- **`GET /projects/`**: List all projects.
- **`POST /projects/`**: Create a new project.
- **`GET /projects/<int:pk>/`**: Retrieve a specific project by ID.
- **`PUT /projects/<int:pk>/`**: Update a specific project by ID.
- **`DELETE /projects/<int:pk>/`**: Delete a specific project by ID.

- **`GET /skills/`**: List all skills.
- **`POST /skills/`**: Create a new skill.
- **`GET /skills/<int:pk>/`**: Retrieve a specific skill by ID.
- **`PUT /skills/<int:pk>/`**: Update a specific skill by ID.
- **`DELETE /skills/<int:pk>/`**: Delete a specific skill by ID.

- **`GET /achievements/`**: List all achievements.
- **`POST /achievements/`**: Create a new achievement.
- **`GET /achievements/<int:pk>/`**: Retrieve a specific achievement by ID.
- **`PUT /achievements/<int:pk>/`**: Update a specific achievement by ID.
- **`DELETE /achievements/<int:pk>/`**: Delete a specific achievement by ID.

- **`GET /contacts/`**: List all contacts.
- **`POST /contacts/`**: Create a new contact.
- **`GET /contacts/<int:pk>/`**: Retrieve a specific contact by ID.
- **`PUT /contacts/<int:pk>/`**: Update a specific contact by ID.
- **`DELETE /contacts/<int:pk>/`**: Delete a specific contact by ID.
