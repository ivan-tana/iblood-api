#Paveway Iblood api project

## How to use this api 
The api is bulid with python using the flask libary and the flask-restful extension
The database is build using flask-sqlalchemy 

## Getting started: configurations and intalls 
Clone the repositorty to a folder
* run "virtualenv venv" to create a virtual enviroment and activate it with "source venv/bin/activate" for linux or "venv/scripts/activate" for windows in your terminal"
* run "pip install -r requirements.txt" to install all the libaries and dependacies used in the project
* run "export FLASK_APP=api" to tell flask where the app is located"
* run "flask create_tables" to create all the database tables 

## If all the above went withdout a problem, then it's time to run the api
There are two way you can run the app
* if you have run the export FLASK_APP command then you can simply run "flask run" to run the api 
* you can also run the app by using the command "python3 run.py" to run the run.py file, if you are using linux you may need to run "python3 run.p
y"

# How the api works
## Creating a user account
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

{ message : user account already exists }

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
* profile_image

## Blood request 
After the admin has verified and approved the account then the user can create and fullfile blood requests 


Blood requets 

A blood request can be created by posting a json object to request/create

The json object should contain the following  

* requested_blood_type
* due _date 

If the creation of the request is successfull the server will send a json object responce containing a message that the request was created successfully  and a 200 status code
{ 
message: request created
}

If the request could not be create the server sends a responce with a 404 status code 
{
message: could not create request 
}

Fullfill a request
All request created are given an id which can be user to access them 
A user  