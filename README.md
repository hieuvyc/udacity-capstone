# Casting Agency
The Casting Agency application is designed to simplify the management of actors, movies, and their respective roles in the entertainment industry. It provides robust tools for administrators to manage these entities while implementing strict role-based access control (RBAC) for secure operations.

# Core Features
### Actors Management:
Add, update, and delete actors.

View actor details, including name, age, and gender.
### Movies Management:

Add, update, and delete movies.

View movie details, including title and release date.

### Role-Based Access Control (RBAC):
#### Casting Assistant: Can view actors and movies.
#### Casting Director: Full access to actors and movies, including creating and deleting movies.

# Note
This project includes the postman collection (casting-agency-onrender.postman_collection.json) used to test APIs, permissions, and roles. Authentication is included in the collection.

### Instructions to set up authentication (only use when token is expired)
- Following README.md in frontend folder to setup the frontend project
- Get the token
  - Go to: http://localhost:8100/
  - Login with username and password to get the token
    - username: hieuvyc@gmal.com -> Casting Director
    - username: 4eyegroup@gmail.com -> Casting Assistant
    - password is given on note submission.


# URL location
https://udacity-capstone-6sdm.onrender.com/

# Local Development 

### Installing Dependencies

#### Python 3.11

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the root project directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight PostgreSQL database.

- Authentication and Authorization: Auth0 for JWT-based secure user authentication and role management.

### .env setup

- Connect local to postgres on render

DATABASE_URL=postgresql://casting_agency_user:54IqhKFgORKdbrKtXWJmfgvvGNW9VyAL@dpg-ctnd671opnds73fmh00g-a.oregon-postgres.render.com/casting_agency_iwl0

- Use for local

DATABASE_NAME=casting_agency

DATABASE_NAME_TEST=casting_agency_test

DATABASE_USER=mac

DATABASE_PASSWORD=

DATABASE_HOST=localhost:5432

CASTING_ASSISTANT_TOKEN=""

CASTING_DIRECTOR_TOKEN =""


### Running the server

From within the project root directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

DEBUG mode, run:

```bash
FLASK_DEBUG=1
```

To run the server, execute:

```bash
flask run --reload 
or
gunicorn app:app
```
The `--reload` flag will detect file changes and restart the server automatically.

# Hosting Instructions

## Step 1: Create a Render Account

## Step 2: Set up a Database Service with Postgres

On the New Postgres page:

1. Enter a name for the new database service: postgres-deployment-example

2. Select an instance type: Free

3. Click Create Database button

## Step 3: Deploy Apps with Render's Web Service

1. Connect your Flask app from GitHub or GitLab repo to the Web Service

2. Connect the Database Service and Web Service

3. Config environment variable

# APIs document
```
#Actors

GET /actors
- Description: Fetches all actors on the platform.
- Request Arguments: None.
- Allowed Users: Executive Producer, Casting Assistant, and Casting Director.
- Required Permission: get:actors
- Response:
{
  "success": true,
  "actors": [
    {
      "id": 1,
      "name": "Tom Cruise",
      "age": 58,
      "gender": "Male"
    },
    {
      "id": 2,
      "name": "Meryl Streep",
      "age": 71,
      "gender": "Female"
    }
  ]
}

POST /actors
- Description: Adds a new actor.
- Request Arguments (JSON body):
{
  "name": "string",
  "age": "integer",
  "gender": "string"
}
- Allowed Users: Executive Producer, Casting Director.
- Required Permission: post:actors
- Response:
{
  "success": true,
  "actor": {
    "id": 3,
    "name": "Robert Downey",
    "age": 56,
    "gender": "Male"
  }
}

PATCH /actors/<actor_id>
- Description: Updates the details of a specific actor.
- Request Arguments (JSON body):
{
  "name": "string",
  "age": "integer",
  "gender": "string"
}
- Allowed Users: Executive Producer, Casting Director.
- Required Permission: patch:actors
- Response:
{
  "success": true,
  "actor": {
    "id": 3,
    "name": "Chris Hemsworth",
    "age": 37,
    "gender": "Male"
  }
}

DELETE /actors/<actor_id>
- Description: Deletes a specific actor.
- Request Arguments: None.
- Allowed Users: Executive Producer, Casting Director.
- Required Permission: delete:actors
- Response:
{
  "success": true,
  "delete": 3
}

#Movies
GET /movies
- Description: Fetches all movies on the platform.
- Request Arguments: None.
- Allowed Users: Executive Producer, Casting Assistant, and Casting Director.
- Required Permission: get:movies
- Response:
{
  "success": true,
  "movies": [
    {
      "id": 3,
      "title": "Avengers: Endgame",
      "release_date": "2019-04-26"
    },
    {
      "id": 5,
      "title": "The Shawshank Redemption",
      "release_date": "1994-09-22"
    }
  ]
}

POST /movies
- Description: Adds a new movie.
- Request Arguments (JSON body):
{
  "title": "string",
  "release_date": "string"
}
- Allowed Users: Executive Producer.
- Required Permission: post:movies
- Response:
{
  "success": true,
  "movie": {
    "id": 6,
    "title": "Inception",
    "release_date": "2010-07-16"
  }
}


PATCH /movies/<movie_id>
- Description: Updates the details of a specific movie.
- Request Arguments (JSON body):
{
  "title": "string",
  "release_date": "string"
}
- Allowed Users: Executive Producer, Casting Director.
- Required Permission: patch:movies
- Response:
{
  "success": true,
  "movie": {
    "id": 6,
    "title": "The Dark Knight",
    "release_date": "2008-07-18"
  }
}

DELETE /movies/<movie_id>
- Description: Deletes a specific movie.
- Request Arguments: None.
- Allowed Users: Executive Producer.
- Required Permission: delete:movies
- Response:
{
  "success": true,
  "delete": 6
}

#Error Handling
- The API returns error messages in the following format:
{
  "success": false,
  "error": 400,
  "message": "Bad request"
}
- 400: Bad Request
- 404: Resource Not Found
- 403: Permission Not Found
- 500: Internal Server Error

```
