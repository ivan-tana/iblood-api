import profile
from .models import User, User_Profile
def get_user(user_id):
    user = User.query.filter_by(id = user_id)

def get_user_profile(user_id):
    profile = User_Profile.query.filter_by(id = user_id).first()

    if not profile:
        data = {
            'first_name': '',
            'last_name': '',
            'birthday': '',
            'blood type': '',
            'image_url':  ''
        }
    else:
        data = {
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'birthday': profile.birthday,
            'blood type': profile.blood_type,
            'image_url':  profile.image_url
        }

    return data