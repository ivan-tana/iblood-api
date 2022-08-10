from .models import User, User_Profile
from api.extensions import db
from flask_restful import abort



def create_user(email, password):

    if not User.query.filter_by(email = email).first():
        try:
            new_user = User(email=email, password = password)
            db.session.add(new_user)
            db.session.commit()

            return True
        except:
            abort(400, message='user already exists')
            return False
        
    return False


def create_user_profile(user_id, data: dict):

    # if user profile already exist update the pofile

    check_profile = User_Profile.query.filter_by(user_id = user_id).first()
    user = User.query.filter_by(id = user_id)
    first_name = data['first_name']
    last_name = data['last_name']
    birthday = data['birthday']
    blood_type = data['blood_type']
    image_url = data['image_url']  

    print(first_name)
    if check_profile:
        profile = User_Profile.query.filter_by(id = user_id)
        profile.update(dict(
            user_id = user_id,
            first_name = first_name,
            last_name = last_name,
            birthday = birthday,
            blood_type = blood_type,
            image_url = image_url)
        )
    
        db.session.commit()
        return True
    else:
        user_profile = User_Profile( 
            user_id = user_id,
            first_name = first_name,
            last_name = last_name,
            birthday = birthday,
            blood_type = blood_type,
            image_url = image_url
        )
        

        db.session.add(user_profile)
        db.session.commit()
        
        

        return True

def delete_profile(user_id):
    profile = User_Profile.query.filter_by(user_id = user_id).delete()
    db.session.commit()
    return True


    
def create_request(user_id, due_date, blood_type):
    pass