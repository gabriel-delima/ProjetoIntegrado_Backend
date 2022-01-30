from flask import Blueprint

from app.password_recovery.controllers import PasswordEmail, PasswordReset

pw_api = Blueprint("pw_api",__name__)

pw_api.add_url_rule(
    "/pw/email",
    view_func=PasswordEmail.as_view('pw_email'),
    methods=['POST'] 
)

pw_api.add_url_rule(
    "/pw/reset/<token>",
    view_func=PasswordReset.as_view('pw_reset'),
    methods=['PATCH'] 
)