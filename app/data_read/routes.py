from flask import Blueprint
from app.data_read.controllers import ( LoadRead )

data_read_api = Blueprint("data_read_api", __name__)

data_read_api.add_url_rule(
    "/data_read/load", 
    view_func= LoadRead.as_view("load_read"),
    methods=["POST"]
)
