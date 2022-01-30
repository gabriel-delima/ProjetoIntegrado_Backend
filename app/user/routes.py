from flask import Blueprint
from app.user.controllers import ( ListUsers,
                                    UserCreate, 
                                    UserCurrent,
                                    UserDetails )

user_api = Blueprint("user_api", __name__)

user_api.add_url_rule(
    "/user/all", 
    view_func= ListUsers.as_view("list_users"),
    methods=["GET"]
)

user_api.add_url_rule(
    "/user/current", 
    view_func= UserCurrent.as_view("user_current"),
    methods=["GET"]
)

user_api.add_url_rule(
    "/user/create", 
    view_func= UserCreate.as_view("user_create"),
    methods=["POST"]
)

user_api.add_url_rule(
    "/user/<int:id>", 
    view_func= UserDetails.as_view("user_details"),
    methods=["GET","PATCH","DELETE"]
)