from functools import partial
from time import time
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.data_read.model import DataRead
from app.data_read.schemas import DataReadSchema
from app.utils.filters import filters

import datetime 

class ListDataReads(MethodView):
    #decorators = [jwt_required()]           #/data_read/all
    def get(self):

        schema = filters.getSchema(
            qs=request.args, 
            schema_cls=DataReadSchema,
            many = True
            ) 
        data_reads = DataRead.query.all()
        return jsonify(schema.dump(data_reads)), 200


class LoadRead(MethodView):                 #/data_read/load
    
    def post(self):
        data = request.json
        schema = DataReadSchema()

        voltage = data["voltage"]
        
        if (voltage >= 0 or voltage < 3.37):
            nivel_bateria = "Bateria Muito Baixa"
        elif (voltage >= 3.37 or voltage < 3.65):
            nivel_bateria = "Bateria Baixa"
        elif (voltage >= 3.65 or voltage < 4):
            nivel_bateria = "Bateria Média"
        elif (voltage >= 4):
            nivel_bateria = "Bateria Alta"
        else:
            nivel_bateria = "Indefinido"
        
        data_read = schema.load({ "uv": data["uv"],
                                  "voltage": data["voltage"],
                                  "risco": data["risco"],
                                  "nivel_bateria": nivel_bateria,
                                  "sensor_id": 1})
        data_read.save()

        return schema.dump(data_read), 200

class DataReadDetails(MethodView):             #/data_read/<int:id>
    
    #decorators = [jwt_required()]

    def get(self,id):
        schema = filters.getSchema(
            qs=request.args,
            schema_cls=DataReadSchema
        )
        data_read = DataRead.query.get_or_404(id)
        return schema.dump(data_read), 200

    def delete(self,id):
        data_read = DataRead.query.get_or_404(id)
        data_read.delete(data_read)
        return {}, 204

class GetLastRead(MethodView):

    #decorators = [jwt_required()]

    def get(self):
        data_reads = DataRead.query.filter_by(sensor_id = 1).order_by("create_time").all()
        if not data_reads:
            return {"error" : "No read on storage"},400 
        most_recent_read = data_reads[len(data_reads)-1]
        if not most_recent_read:
            return {"error" : "Error when trying to get most recent read"}, 400
    
        schema = filters.getSchema(
            qs=request.args, 
            schema_cls=DataReadSchema,
            many = False
            ) 
        
        return schema.dump(most_recent_read), 200