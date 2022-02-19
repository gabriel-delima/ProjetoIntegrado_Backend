import datetime
from app.extensions import ma
from app.data_read.model import DataRead

delta = datetime.timedelta( hours=3 )

class DataReadSchema( ma.SQLAlchemySchema):

    class Meta:
        model = DataRead
        load_instance = True
        ordered = True

    data_read_id = ma.Integer(dump_only=True)
    risco = ma.String(required=True)
    uv = ma.Float(required=True)
    voltage = ma.Float(required=True)
    sensor_id = ma.Integer(required=True)  
    nivel_bateria = ma.String(required=True)               

    create_time = ma.DateTime(dump_only=True)
    update_time = ma.DateTime(dump_only=True)   