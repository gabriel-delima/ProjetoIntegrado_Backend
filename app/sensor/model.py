from app.extensions import db
from app.models import BaseModel

class Sensor(BaseModel):
    __tablename__ = 'sensor'

    sensor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))