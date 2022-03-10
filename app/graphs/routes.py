from flask import Blueprint
from app.graphs.controllers import (ManyDaysGraph,
                                    OneDayGraph,
                                    MaxUvByDayGraph)

graph_api = Blueprint("graph_api", __name__)

graph_api.add_url_rule(
    "/graph/many_days/<int:number_of_days_before>", 
    view_func= ManyDaysGraph.as_view("ManyDaysGraph"),
    methods=["GET"]
)

graph_api.add_url_rule(
    "/graph/one_day/<int:number_of_days_before>", 
    view_func= OneDayGraph.as_view("OneDayGraph"),
    methods=["GET"]
)

graph_api.add_url_rule(
    "/graph/max_uv/<int:number_of_days_before>", 
    view_func= MaxUvByDayGraph.as_view("MaxUvByDayGraph"),
    methods=["GET"]
)