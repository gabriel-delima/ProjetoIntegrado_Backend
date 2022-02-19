from email.policy import default
from app.extensions import ma
from app.daily_tip.model import DailyTip

class DailyTipSchema( ma.SQLAlchemySchema):

    class Meta:
        model = DailyTip
        load_instance = True
        ordered = True

    daily_tip_id = ma.Integer(dump_only=True)
    tip = ma.String(required=True)
    already_shown = ma.Boolean(dump_only = True)

    create_time = ma.DateTime(dump_only=True)
    update_time = ma.DateTime(dump_only=True)