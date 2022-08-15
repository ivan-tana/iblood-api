from api.extensions import db 


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), unique =True, nullable=False )
    password = db.Column(db.String(255), nullable = False)
    is_confirm = db.Column(db.Boolean, default = False)
    is_active = db.Column(db.Boolean, default = False)
    is_admin = db.Column(db.Boolean, default = False)

class User_Profile(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id =  db.Column(db.Text, unique = True)
    first_name = db.Column(db.String(60), nullable=False )
    last_name = db.Column(db.String(60), nullable=False )
    birthday = db.Column(db.String(60), nullable=False )
    blood_type = db.Column(db.String(60), nullable=False )
    image_url =db.Column(db.Text,  )



class Request(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Text, unique = True)
    patient_name = db.Column(db.String(60), nullable=False )
    blood_type = db.Column(db.String(60), nullable=False )
    due_date = db.Column(db.String(60), nullable=False )
    fullfilled = db.Column(db.Boolean, default = False)

