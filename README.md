# Perpex Notes API
================

This is a simple Notes API built with Django and Django REST Framework (DRF), developed as my first project during my internship at Perpex.

The API supports user authentication using Token Authentication, allowing users to register, log in, and manage their personal notes (CRUD operations).

-------------------------------------
Features
--------

- User Registration & Login
- Token-based Authentication
- Create, Read, Update & Delete Notes
- DRF-powered JSON API responses
- RESTful Endpoints

-------------------------------------
Tech Stack
----------

- Python 3.x
- Django
- Django REST Framework
- DRF Authtoken
- SQLite (default, but switchable)

-------------------------------------
Installation & Setup
---------------------

1. Clone the repository

    git clone https://github.com/your-username/perpex-notes-api.git
    cd perpex-notes-api

2. Create and activate virtual environment

    python -m venv venv
    source venv/bin/activate       # On Windows: venv\Scripts\activate

3. Install dependencies

    pip install -r requirements.txt

4. Apply migrations

    python manage.py migrate

5. Run the server

    python manage.py runserver

-------------------------------------
API Authentication
-------------------

This API uses Token Authentication. After logging in, include your token in the headers like this:

    Authorization: Token your_token_here

-------------------------------------
API Endpoints Overview
-----------------------

Method | Endpoint            | Description              | Auth Required
------ | ------------------- | ------------------------ | --------------
POST   | /api/register/      | Register a new user      | No
POST   | /api/login/         | Login and get token      | No
GET    | /api/notes/         | Get all user notes       | Yes
POST   | /api/notes/         | Create a new note        | Yes
GET    | /api/notes/<id>/    | Retrieve a single note   | Yes
PUT    | /api/notes/<id>/    | Update an existing note  | Yes
DELETE | /api/notes/<id>/    | Delete a note            | Yes

-------------------------------------
Author
------

Buchi Rex-David  
Intern @ Perpex  
Email: rhexmilia06@gmail.com  
LinkedIn: https://linkedin.com/in/buchi-rex-david  
GitHub: https://github.com/RexDavid06

-------------------------------------
License
-------

This project is open source and available under the MIT License.
