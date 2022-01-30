from app.extensions import db
from app.models import BaseModel

class DataRead(BaseModel):
    __tablename__ = 'data_read'

    data_read_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(64), nullable=False)
    value = db.Column(db.Float, nullable = False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.sensor_id'))
