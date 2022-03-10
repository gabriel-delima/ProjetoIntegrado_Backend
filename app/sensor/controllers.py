from functools import partial
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.sensor.model import Sensor
from app.sensor.schemas import SensorSchema
from app.utils.filters import filters


class ListSensors(MethodView):
    decorators = [jwt_required()]           #/sensor/all
    def get(self):

        schema = filters.getSchema(
            qs=request.args, 
            schema_cls=SensorSchema,
            many = True
            ) 
        sensors = Sensor.query.all()
        return jsonify(schema.dump(sensors)), 200



class SensorCreate(MethodView):              #/sensor/create

    def post(self):
        schema = SensorSchema()
        sensor = schema.load(request.json)
        sensor.save()

        return schema.dump(sensor), 201



class SensorDetails(MethodView):             #/sensor/<int:id>

    def get(self,id):
        schema = filters.getSchema(
            qs=request.args,
            schema_cls=SensorSchema
        )
        sensor = Sensor.query.get_or_404(id)
        return schema.dump(sensor), 200

    def patch(self,id):
        sensor = Sensor.query.get_or_404(id)
        schema = SensorSchema()
        sensor = schema.load(request.json, instance = sensor, partial=True)
        sensor.save()
        return schema.dump(sensor)

    def delete(self, id):
        sensor = Sensor.query.get_or_404(id)
        sensor.delete(sensor)
        return {}, 204