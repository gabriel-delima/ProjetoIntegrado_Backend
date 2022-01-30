from functools import partial
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.data_read.model import DataRead
from app.data_read.schemas import DataReadSchema, LoadReadSchema
from app.utils.filters import filters


class LoadRead(MethodView):                 #/data_read/load
    
    def post(self):
        data = request.json
        read = LoadReadSchema().load(data)
        schema = DataReadSchema()
        
        data_read_1 = schema.load({ "type": "uv",
                                    "value": data["uv"],
                                    "sensor_id": 1})
        data_read.save()
        
        data_read_2 = schema.load({ "type": "voltage",
                                    "value": data["voltage"],
                                    "sensor_id": 1})
        data_read.save()


        return {"data_read_1" : schema.dump(data_read_1), "data_read_2" : schema.dump(data_read_2)}, 200