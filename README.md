# Car API
A technical recruitement task to build a REST API that is used to manage an aircraft fleet and flights schedule


## Technologies
* Python 3.9
* Django 3.1.6
* Django REST Framework 3.12.2

## Setup
To run this project you have to have Python version 3.9 installed 

Enter the project's root directory

Create a virtual environment
and execute commands through command line

`pip install -r requirements.txt`

After the required packages are installed use commands

```
python manage.py migrate
python manage.py runserver
```

The development server should start and the app should be accessible at [localhost:8000](localhost:8000) or the local ip address of the machine

## URLs

/aircrafts/ : GET - list of all aircrafts, POST - add a new aircraft, 'serial' and 'manufacturer' in request

/aircrafts/{id} : GET - details of an aircraft with id = {id}, DELETE - delete an aircraft with id = {id}, PUT and PATCH methods also avaliable

/flights/ : GET - list of all flights, POST - add a new flight, 'departure_time', 'arrival_time', 'departure_icao', 'arrival_icao', 'aircraft' in request

/flights/{id} : GET - details of a flight with id = {id}, DELETE - delete a flight with id = {id}, PUT and PATCH methods also avaliable
