from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import HTTPException
from flask import json


class AppExceptions(object):

    """Return JSON errors"""

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        @app.errorhandler(HTTPException)
        def handler(e):
            response = e.get_response()
            response.data = json.dumps({'code': e.code,
                                        'name': e.name,
                                        'description': e.description})
            response.content_type = 'application/json'
            response.status_code = e.code
            return response

        @app.errorhandler(ValidationError)
        def handler(e):
            return e.messages, 400


global_exceptions = AppExceptions()