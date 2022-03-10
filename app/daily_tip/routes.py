from flask import Blueprint
from app.daily_tip.controllers import ( ListDailyTips,
                                        DailyTipCreate, 
                                        DailyTipDetails,
                                        DailyTipRandom)

daily_tip_api = Blueprint("daily_tip_api", __name__)

daily_tip_api.add_url_rule(
    "/daily_tip/all", 
    view_func= ListDailyTips.as_view("list_daily_tips"),
    methods=["GET"]
)

daily_tip_api.add_url_rule(
    "/daily_tip/create", 
    view_func= DailyTipCreate.as_view("daily_tip_create"),
    methods=["POST"]
)

daily_tip_api.add_url_rule(
    "/daily_tip/<int:id>", 
    view_func= DailyTipDetails.as_view("daily_tip_details"),
    methods=["GET","PATCH","DELETE"]
)

daily_tip_api.add_url_rule(
    "/daily_tip/random", 
    view_func= DailyTipRandom.as_view("daily_random_tip"),
    methods=["GET"]
)