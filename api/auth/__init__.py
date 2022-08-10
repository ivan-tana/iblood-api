from email import message
from flask import request
from flask_restful import abort
from .token import encode, decode
from api.models.models import User
from werkzeug.security import check_password_hash


def token_required(f):
    def wrapper(*args, **kwargs):
        
        
        if not 'x-access-token' in request.headers:
            abort(401, message= 'access token required')
        
        
        token = request.headers['x-access-token']
        if verified_token(token):
            data = decode(token)
            user = User.query.filter_by(email = data['email']).first()
            current_user = user
            return f(*args, **kwargs, current_user = current_user)
    return wrapper


def verified_token(token):
    data = decode(token)
    # check data
    user = User.query.filter_by(email = data['email']).first()
    if not user:
        abort(401, message='user not found')
   
    if check_password_hash(user.password, data['password']):
        
        return True
    else:
        abort(401, message='invalid token')

    return False

