from flask import Blueprint
from app.data_read.controllers import ( ListDataReads,
                                        LoadRead,
                                        DataReadDetails,
                                        GetLastRead)

data_read_api = Blueprint("data_read_api", __name__)

data_read_api.add_url_rule(
    "/data_read/all", 
    view_func= ListDataReads.as_view("list_data_reads"),
    methods=["GET"]
)

data_read_api.add_url_rule(
    "/data_read/load", 
    view_func= LoadRead.as_view("load_read"),
    methods=["POST"]
)

data_read_api.add_url_rule(
    "/data_read/<int:id>", 
    view_func= DataReadDetails.as_view("data_read_details"),
    methods=["GET","DELETE"]
)

data_read_api.add_url_rule(
    "/data_read/last", 
    view_func= GetLastRead.as_view("get_last_read"),
    methods=["GET"]
)