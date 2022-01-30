from app.extensions import ma
from app.data_read.model import DataRead

class DataReadSchema( ma.SQLAlchemySchema):

    class Meta:
        model = DataRead
        load_instance = True
        ordered = True

    data_read_id = ma.Integer(dump_only=True)
    type = ma.String(required=True)
    value = ma.Float(dump_only=True)
    sensor_id = ma.Integer(dump_only=True)

    create_time = ma.DateTime(dump_only=True)
    update_time = ma.DateTime(dump_only=True)

class LoadReadSchema(ma.Schema):
    read = ma.String(required=True)

