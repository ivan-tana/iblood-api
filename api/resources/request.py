from flask_restful import reqparse, Resource
from api.auth import token_required


request_perser = reqparse.RequestParser()
request_perser.add_argument('due_date', required=True, help='missing due_date')

class Request(Resource):
    def get(self, request_id):
        pass

   
    def put(self):
        pass

    def delete(self, request_id):
        pass
    @token_required
    def post(self, current_user):
        args = request_perser.parse_args()


        pass    
