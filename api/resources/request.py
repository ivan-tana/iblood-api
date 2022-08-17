from flask_restful import reqparse, Resource
from api.auth import token_required

from api.models.manupulations import create_request, fullfill_request
from api.models.queries import get_all_request

request_perser = reqparse.RequestParser()
request_perser.add_argument('patient_name', required=True, help='Missing patient_name')
request_perser.add_argument('blood_type', required=True, help='Missing blood_type')
request_perser.add_argument('due_date', required=True, help='missing due_date')


class Request(Resource):
    @token_required
    def get(self, current_user):
        return get_all_request()
    @token_required
    def post(self, current_user):
        args = request_perser.parse_args()
        user_id = current_user.id
        patient_name = args['patient_name']
        blood_type = args['blood_type']
        due_date = args['due_date']

        if create_request(user_id,due_date,blood_type,patient_name):
            return {'message': 'request created'}
        return {'message':'could not create request'} 


class Specific_Request(Resource):
    @token_required
    def post(self, current_user, request_id):

        if fullfill_request(request_id,current_user.id):
            return {
                "message": "request fullfilled"
            }
        return {'message': 'could not fullfilled request'}