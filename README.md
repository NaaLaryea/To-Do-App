# Simple Todo List Application

This project is a simple Todo List application, which allows a user to add tasks to a todo list, edit and update task items, view changes in the list, and mark out a task when it is completed. 

This application is user specific, and as such requires anyone who would like to use it, to first register, by creating a new account. Subsequently a user may log in with the account details he/she registered with, which is a username and password.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

Ensure to have the following installed:

- Python 3
- virtual environment
- A web browser

### Installing
The following steps are required to install the appliaction:

#### 1. Clone the repository
git@github.com:NaaLaryea/To-Do-App.git

#### 2. Create your own virtual environment
python3 -m venv venv
source venv/bin/activate

#### 3. Install your requirements
pip install -r requirements.txt

#### 4. Make your migrations
python manage.py makemigrations
python manage.py migrate

#### 5. Create a superuser
python manage.py createsuperuser

#### 6. Run the server
python manage.py runserver

## Built With

* [Django](https://djangoproject.com/) - The web framework used


## Authors

* **Dorcas Adjeley Laryea** - *Initial work* - [NaaLaryea](https://github.com/NaaLaryea)

