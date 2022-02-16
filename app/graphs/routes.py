from flask import Blueprint
from app.graphs.controllers import (ManyDaysGraph,
                                    OneDayGraph)

graph_api = Blueprint("graph_api", __name__)

graph_api.add_url_rule(
    "/graph/many_days/<int:number_of_days_before>", 
    view_func= ManyDaysGraph.as_view("TodayGraph"),
    methods=["GET"]
)

graph_api.add_url_rule(
    "/graph/one_day/<int:number_of_days_before>", 
    view_func= OneDayGraph.as_view("Graph"),
    methods=["GET"]
)