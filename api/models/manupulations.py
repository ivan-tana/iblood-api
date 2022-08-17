from email import message
from .models import User, User_Profile, Request
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


    
def create_request(user_id, due_date, blood_type, patient_name):
    new_request = Request(
        user_id = user_id,
        patient_name = patient_name,
        blood_type = blood_type,
        due_date = due_date
    )

    try: 
        db.session.add(new_request)
        db.session.commit()
    except:
        abort(400, message='could not create request ')
    return True

def delete_request(request_id):
    request  = Request.query.filter_by(id = request_id).delete()
    db.session.commit()
    return True

def fullfill_request(request_id, user_id):
    request  = Request.query.filter_by(id = request_id).first()
    if int(request.user_id) == int(user_id):
        print('users are the same')
        abort(400, message='request cannot be fullfilled by the current user')
        return False
    if request.fullfilled == True:
        abort(400, message ='request has already been fullfilled')
        return False
    else:
        print(user_id, request.user_id)
        rq = Request.query.get(request_id)
        rq.fullfilled = True
        db.session.commit()
        return True
    return False