# User-transaction-API Project" 

This project is a Django-based application that manages users and their transactions, providing API endpoints for CRUD operations, an admin interface for database management, and a statistics dashboard for transaction summaries.

## Technology stack

* Backend:
  - Language: Python 3 
  - Framework: Django 
  - Database: Postgresql 
* Dependency Management: pip
* Containerization: Docker
* Virtual Environment: venv
* Database Migrations: Django Migrations
* Collaboration and Version Control:
  - Version Control System: Git
  - Repository Hosting: GitHub
* API Documentation: Swagger
* Environment Variables: .env
* Other: requirements.txt

## Installation

Python3 must be already installed

```shell
# Local setup
# Clone the repository:
git clone https://github.com/oleg-potichnyi/user-transaction-API
# Change directory to the project folder:
cd user-transaction-API
# Set up a virtual environment:
python3 -m venv venv
# Activate the virtual environment on Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
# Install dependencies:
pip install -r requirements.txt
# Environment variables:
# Duplicate the .env.sample file and rename it to .env.
cp .env.sample .env
# Fill in the variables in the .env file with your actual configuration values.
# Run this command to apply migrations and update the database schema:
python manage.py migrate
# Start the development server:
python manage.py runserver
```
```shell
# Start the Application via Docker
# Clone the repository:
git clone https://github.com/oleg-potichnyi/user-transaction-API
# Change directory to the project folder:
cd user-transaction-API
# Setup via Docker
# Build the Docker Containers:
docker-compose build
# Start the Docker Containers:
docker-compose up
# Stopping the Docker Containers:
# To stop the Docker containers, use the following command:
docker-compose down
```
## Features

* Database Management: Creates and manages a database with "users" and "transactions" tables.
* API Endpoints:
   - Add User: Accepts a username and returns the ID of the created user.
   - Get User: Retrieves a user's ID, username, and all associated transactions.
   - Get All Users: Returns all users and their respective transactions.
   - Add Transaction: Records a transaction by accepting a user ID, transaction type, and amount.
* Admin Interface: Allows viewing, editing, and deleting database entries through a web-based admin panel.

## Admin credentials

```shell
Name: Oleg
password: admin12345
```
