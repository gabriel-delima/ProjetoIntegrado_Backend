from functools import partial
from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from app.daily_tip.model import DailyTip
from app.daily_tip.schemas import DailyTipSchema
from app.utils.filters import filters

from random import randrange


class ListDailyTips(MethodView):
    #decorators = [jwt_required()]           #/daily_tip/all
    def get(self):

        schema = filters.getSchema(
            qs=request.args, 
            schema_cls=DailyTipSchema,
            many = True
            ) 
        daily_tips = DailyTip.query.all()
        return jsonify(schema.dump(daily_tips)), 200



class DailyTipCreate(MethodView):              #/daily_tip/create
    #decorators = [jwt_required()]
    def post(self):
        schema = DailyTipSchema()
        daily_tip = schema.load(request.json)
        daily_tip.save()

        return schema.dump(daily_tip), 201



class DailyTipDetails(MethodView):             #/daily_tip/<int:id>
    #decorators = [jwt_required()]
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


class DailyTipRandom(MethodView):             #/daily_tip/random

    #decorators = [jwt_required()]
    def get(self):
        schema = filters.getSchema(
            qs=request.args,
            schema_cls=DailyTipSchema
        )
        daily_tips = DailyTip.query.filter_by(already_shown = False).all()

        if (len(daily_tips) == 0):
            if (len(DailyTip.query.all()) == 0):
                return {"error" : "No tip registered."}, 400
            else: 
                aux_daily_tips = DailyTip.query.all()
                for i in aux_daily_tips:
                    i.already_shown = False
                    i.save()
                    daily_tips = DailyTip.query.filter_by(already_shown = False).all()

        index = randrange(len(daily_tips))

        daily_tip = daily_tips[index]
        daily_tip.already_shown = True
        daily_tip.save()

        return schema.dump(daily_tip), 200