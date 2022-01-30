from flask import Blueprint
from app.sensor.controllers import (ListSensors,
                                    SensorCreate, 
                                    SensorDetails)

sensor_api = Blueprint("sensor_api", __name__)

sensor_api.add_url_rule(
    "/sensor/all", 
    view_func= ListSensors.as_view("list_sensors"),
    methods=["GET"]
)

sensor_api.add_url_rule(
    "/sensor/create", 
    view_func= SensorCreate.as_view("sensor_create"),
    methods=["POST"]
)

sensor_api.add_url_rule(
    "/sensor/<int:id>", 
    view_func= SensorDetails.as_view("sensor_details"),
    methods=["GET","PATCH","DELETE"]
)