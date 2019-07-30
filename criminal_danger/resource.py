from flask_restful import Resource, reqparse
from criminal_danger.mocked_data import street_list, criminal_danger_list
from criminal_danger.model import StreetResponse, Street, CriminalDangerResponse
from flask import request
from criminal_danger.data import save_street, verify_existence_street, update_street


class StreetResource(Resource):
    def get(self):
        result = []
        args = request.args
        if args['id'] == None:
            result = StreetResponse(street_list).build_friendly()
        else:
            id_list = str.split(args['id'], ',')
            result = list(filter(lambda i: str(i['id']) in id_list, StreetResponse(street_list).build_friendly()))
        return {'status': 'success', 'data': result}


    def post(self):
        json_result = request.get_json()
        for item in json_result:
            # here we don't need to pass id but this can be implemented easy with database implementation
            street = Street(item["first_house"], item["second_house"], 1)
            if not verify_existence_street(street):
                save_street(street)
        return {'status': 'success', 'data': StreetResponse(street_list).build_friendly()}

    def put(self):
        json_result = request.get_json()
        for item in json_result:
            # here we don't need to pass id but this can be implemented easy with database implementation
            street = Street(item["first_house"], item["second_house"], 1)
            if not verify_existence_street(street):
                save_street(street)
            else:
                update_street(street)
        return {'status': 'success', 'data': StreetResponse(street_list).build_friendly()}


    def delete(self):
        result = []
        args = request.args
        if args['id'] == None:
            result = StreetResponse(street_list).build_friendly()
        else:
            id_list = str.split(args['id'], ',')
            result = list(filter(lambda i: str(i['id']) in id_list, StreetResponse(street_list).build_friendly()))
        return {'status': 'success', 'data': True}



class CriminalDangerResource(Resource):
    def get(self):
        result = []
        args = request.args
        if args['id'] == None:
            result = CriminalDangerResponse.build_friendly(criminal_danger_list)
        else:
            id_list = list(map(lambda i: "street_" + i, str.split(args['id'], ',')))
            result = list(filter(lambda i: str(i['street_name']) in id_list,
                                 CriminalDangerResponse.build_friendly(criminal_danger_list)))
        return {'status': 'success', 'data': result}