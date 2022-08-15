from api.extensions import api


from .user import Create_User, User_profile, Login
from .request import Request, Specific_Request

api.add_resource(Create_User, '/signup')
api.add_resource(User_profile, '/profile')
api.add_resource(Login, '/login')
api.add_resource(Request, '/request')
api.add_resource(Specific_Request, '/request/<request_id>')
