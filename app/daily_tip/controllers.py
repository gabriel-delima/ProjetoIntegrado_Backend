from functools import partial
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.daily_tip.model import DailyTip
from app.daily_tip.schemas import DailyTipSchema
from app.utils.filters import filters


class ListDailyTips(MethodView):
    decorators = [jwt_required()]           #/daily_tip/all
    def get(self):

        schema = filters.getSchema(
            qs=request.args, 
            schema_cls=DailyTipSchema,
            many = True
            ) 
        daily_tips = DailyTip.query.all()
        return jsonify(schema.dump(daily_tips)), 200



class DailyTipCreate(MethodView):              #/daily_tip/create

    def post(self):
        schema = DailyTipSchema()
        daily_tip = schema.load(request.json)
        daily_tip.save()

        return schema.dump(daily_tip), 201



class DailyTipDetails(MethodView):             #/daily_tip/<int:id>

    def get(self,id):
        schema = filters.getSchema(
            qs=request.args,
            schema_cls=DailyTipSchema
        )
        daily_tip = DailyTip.query.get_or_404(id)
        return schema.dump(daily_tip), 200

    def patch(self,id):
        daily_tip = DailyTip.query.get_or_404(id)
        schema = DailyTipSchema()
        daily_tip = schema.load(request.json, instance = daily_tip, partial=True)
        daily_tip.save()
        return schema.dump(daily_tip)

    def delete(self, id):
        daily_tip = DailyTip.query.get_or_404(id)
        daily_tip.delete(daily_tip)
        return {}, 204