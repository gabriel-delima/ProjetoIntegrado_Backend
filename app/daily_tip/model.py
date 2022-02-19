from email.policy import default
from app.extensions import db
from app.models import BaseModel

class DailyTip(BaseModel):
    __tablename__ = 'daily_tip'

    daily_tip_id = db.Column(db.Integer, primary_key=True)
    tip = db.Column(db.String(264), nullable=False)
    already_shown = db.Column(db.Boolean, default = False)