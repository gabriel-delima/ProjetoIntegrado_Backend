from flask import Blueprint

from app.auth.controllers import Login, TokenRefresh

auth_api = Blueprint("auth_api",__name__)

auth_api.add_url_rule(
    "/login",
    view_func=Login.as_view('login'),
    methods=['POST'] 
)

auth_api.add_url_rule(
    "/refresh",
    view_func=TokenRefresh.as_view('refresh'),
    methods=['GET'] 
)