from api.extensions import api


from .user import Create_User, User_profile, Login

api.add_resource(Create_User, '/user/signup')
api.add_resource(User_profile, '/user/profile')
api.add_resource(Login, '/user/login')

