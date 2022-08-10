from flask_restful import Resource, reqparse, abort
from werkzeug.security import generate_password_hash, check_password_hash
import re
from api.auth import token_required
from api.auth.token import encode

# import models
from api.models.models import User

# import manupulations to the database
from api.models.manupulations import create_user , create_user_profile, delete_profile

from api.models.queries import get_user_profile



# validate email
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def EmailisValid(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False


# all request aguments and their validations
parser = reqparse.RequestParser()

parser.add_argument('email', required = True, help ='Missing the user email in the json body')
parser.add_argument('password', required = True, help = 'Missing password in the json body')




def abort_if_invalid_email(email):
    if not EmailisValid(email):
        abort(400, message= f'{email} is an invalid email address')

def abort_if_password_lessthan_6(password):
    if len(password) < 6:
        abort(400, message='password is too short')



users = []


class Create_User(Resource):

    def get(self, **kwargs):
        return users

    def post(self, **kwargs):
        # check if all the infomation was passsed and return a 404 status code 
        args = parser.parse_args()
        email = args['email']
        password = args['password']
        abort_if_invalid_email(email)
        abort_if_password_lessthan_6(password)

        hash_password = generate_password_hash(password)
        # create user 


        if create_user(email, hash_password):
            return encode({
                'email':email,
                'password': password
            })

        return  {'message': 'could not create user'}, 404



profile_parser = reqparse.RequestParser()

profile_parser.add_argument('first_name', required = True, help = 'Missing first name')
profile_parser.add_argument('last_name', required = True, help = 'Missing last name')
profile_parser.add_argument('birthday', required = True, help = 'Missing birthday')
profile_parser.add_argument('blood_type', required = True, help = 'Missing blood_type')
profile_parser.add_argument('image_url', required = True, help = 'Missing image_url')


class User_profile(Resource):
    @token_required
    def get(self, current_user):
        user_profile = get_user_profile(current_user.id)
        return user_profile
    
    @token_required
    def post(self, current_user):
        args = profile_parser.parse_args()
        data = {
        "first_name":args['first_name'],
        "last_name":args['last_name'],
        "birthday":args['birthday'],
        "blood_type" :args['blood_type'],
        "image_url" :args['image_url']
        }


        if create_user_profile(current_user.id, data):
            return {'message': 'profile created'}
        return {'message': 'could not create profile'}, 400

    @token_required
    def delete(self, current_user):
        if delete_profile(current_user.id):
            return {'message': 'profile deleted'}
        return {'message': 'could not delete profile'}, 400



login_parser = reqparse.RequestParser()
login_parser.add_argument('email', required=True, help='missing email')
login_parser.add_argument('password', required=True, help='missing password')

class Login(Resource):
    def post(self):
        args = login_parser.parse_args()
        email = args['email']
        abort_if_invalid_email(email)
        password = args['password']
        abort_if_password_lessthan_6(password)

        user = User.query.filter_by(email = email).first()
        if user and check_password_hash(user.password, password):
            return encode({
                'email': email,
                'password': password}
            )
        return {'message': 'invalid login details'}, 400
