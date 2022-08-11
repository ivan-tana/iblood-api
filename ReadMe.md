#Paveway Iblood api project

## How to use this api 
The api is bulid with python using the flask libary and the flask-restful extension
The database is build using flask-sqlalchemy 

## Getting started: configurations and intalls 
Clone the repositorty to a folder
*run "virtualenv venv" to create a virtual enviroment and activate it with "source venv/bin/activate" for linux or "venv/scripts/activate" for windows in your terminal"
*run "pip install -r requirements.txt" to install all the libaries and dependacies used in the project
*run "export FLASK_APP=api" to tell flask where the app is located"
*run "flask create_tables" to create all the database tables 

## If all the above went withdout a problem, then it's time to run the api
There are two way you can run the app
*if you have run the export FLASK_APP command then you can simply run "flask run" to run the api 
*you can also run the app by using the command "python3 run.py" to run the run.py file, if you are using linux you may need to run "python3 run.p
y"

# How the api works