import jwt 
from api.bin.settings import SECRET_KEY


def encode(data: dict):
    encoded_data = jwt.encode(data, SECRET_KEY, algorithm='HS256' )
    return encoded_data

def decode(encoded_data):
    data = jwt.decode(encoded_data, SECRET_KEY ,algorithms=['HS256',])
    return data