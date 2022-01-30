from app.extensions import ma
from app.sensor.model import Sensor

class SensorSchema( ma.SQLAlchemySchema):

    class Meta:
        model = Sensor
        load_instance = True
        ordered = True

    sensor_id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    user_id = ma.Integer(required=True)

    create_time = ma.DateTime(dump_only=True)
    update_time = ma.DateTime(dump_only=True)