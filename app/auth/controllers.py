from flask.views import MethodView
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, jwt_required
from flask import request

from app.auth.schemas import LoginSchema
from app.user.model import User


class Login(MethodView):        #/login
    def post(self):
        schema = LoginSchema()
        data = schema.load(request.json)

        user = User.query.filter_by(email = data['email']).first()

        if user and user.verify_password(data['password']):
            token = create_access_token(    
                                        identity = user.user_id, 
                                        expires_delta=timedelta(minutes=10000), 
                                        fresh=True )

            refresh_token = create_refresh_token(   
                                            identity=user.user_id, 
                                            expires_delta=timedelta(minutes=10000))
            return {    
                        "name": user.name,
                        "token": token,
                        "refresh_token": refresh_token
                    }, 200
        else:
            return {"error": "Invalid E-mail or Password"}, 401




class TokenRefresh(MethodView):

    decorators = [jwt_required(refresh=True)]

    def get(self):              # /refresh

        received_token = get_jwt()

        user = User.query.get_or_404(received_token["sub"])
        token = create_access_token(    
                                    identity = user.user_id, 
                                    expires_delta=timedelta(minutes=10000), 
                                    fresh=False )

        refresh_token = create_refresh_token(   
                                        identity=user.user_id, 
                                        expires_delta=timedelta(minutes=10000),
                                        additional_claims={"user_type" : "user"})
        return {    
                    "name": user.name,
                    "token": token,
                    "refresh_token": refresh_token
                }, 200