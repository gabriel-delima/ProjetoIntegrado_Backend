from functools import partial
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.data_read.model import DataRead
from app.data_read.schemas import DataReadSchema, LoadReadSchema
from app.utils.filters import filters


class LoadRead(MethodView):                 #/data_read/load
    
    def post(self):
        read = LoadReadSchema().load(request.json)
        schema = DataReadSchema
        schema.load({ "type": "uv",
                      "value": 31,
                      "sensor_id": 1})
                      
        return {"leitura":read}, 200