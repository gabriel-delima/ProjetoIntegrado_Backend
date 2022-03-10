from app.extensions import db
from app.models import BaseModel

class DataRead(BaseModel):
    __tablename__ = 'data_read'

    data_read_id = db.Column(db.Integer, primary_key=True)
    risco = db.Column(db.String(64), nullable=False)
    uv = db.Column(db.Float, nullable = False)
    voltage = db.Column(db.Float, nullable = False)
    nivel_bateria = db.Column(db.String(64), nullable=False)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.sensor_id'))                  
