#Paveway Iblood api project

## How to use this api 
The api is bulid with python using the flask libary and the flask-restful extension
The database is build using flask-sqlalchemy 

## Getting started: configurations and intalls 
Clone the repositorty to a folder
* run the command below to create a virtual enviroment
    virtualenv venv
And activate it with 
for linux

    Source venv/bin/activate
    
for windows

    venv/scripts/activate

* run "pip install -r requirements.txt" to install all the libaries and dependacies used in the project

    pip install -r requirements.txt

* run "export FLASK_APP=api" to tell flask where the app is located"

    export FLASK_APP=api

* run "flask create_tables" to create all the database tables 

    flask create_tables

## If all the above went withdout a problem, then it's time to run the api
There are two way you can run the app
* if you have run the export FLASK_APP command then you can simply run "flask run" to run the api 
    
    flask run" to run the api

* you can also run the app by using the command "python3 run.py" to run the run.py file, if you are using linux you may need to run "python3 run.py"
    
    python3 run.py
    python3 run.py

# How the api works
## Creating a user account

### Note: The request send to the sever except for the login and create user route must all contain an access token in the header of the request
Creating a new user a count is done in two steps first the user auth and then the user profile 
User auth
The user profile is created by posting a json object to /user/signup 
The json object most contain the following infomations
* email
* password 

example:

    {
        "email":"useremail",
        "password": "userpassword"
    }

If the account is created successfully the response will contain an auth token generated using the username and password and a 200 status code 

    { 
       "token": "token string"
    }

If the user account alrady exist this will result in  responce with a 404 status code and a message indicating the user accounts already exists

    {
        "message" :"could not create user"
    }

After the user account is created an auth token is generated using the user email and password and sent back as a responce in the HTTP basic auth header 

The auth token should be used for any request by the account it was generated fro, each token expires ofter 3 days 

With the user account created the auth token received can be us to identify the user on the server 
User profile
The user profile is created by posting a json token with the auth token in the HTTP header to user/profile

The user profile token should contain the following 
* first_name
* last_name
* birthday
* blood_type
* image_url

Example 

    {
        "first_name": "user first name",
        "last_name": "user last name",
        "birthday": "user birthday",
        "blood type": "user blood type",
        "image url": "user profile image link"
    }

the user profile can be updated by sending a post request to the user/profile with all the infomation field in and an edit to the field you want to edit

Example editing the user name
    {
        "first_name": "user first name edited",
        "last_name": "user last name",
        "birthday": "user birthday",
        "blood type": "user blood type",
        "image url": "user profile image link"
    }

To view the user name send a post request to the user/profile link and you will get the user profile information

    {
        "first_name": "user first name",
        "last_name": "user last name",
        "birthday": "user birthday",
        "blood type": "user blood type",
        "image url": "user profile image link"
    }

if the user profile has been deleted or not created you will get  a response with the fileds fro the user information left blank

## Blood request 
After the admin has verified and approved the account then the user can create and fullfile blood requests 
