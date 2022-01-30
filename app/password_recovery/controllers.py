from flask.views import MethodView
from datetime import timedelta
from flask_mail import Message
from flask_jwt_extended import create_access_token, decode_token
from flask import request, render_template

from app.password_recovery.schemas import PasswordEmailSchema, PasswordResetSchema
from app.user.model import User
from app.extensions import mail


class PasswordEmail(MethodView):                    #/pw/email
    def post(self):
        schema = PasswordEmailSchema()
        data = schema.load(request.json)

        user = User.query.filter_by(email = data['email']).first()
        if user:
            token = create_access_token(identity = user.user_id,expires_delta=timedelta(minutes=60))
        
        else:
            return {"error": "No account registered with this email"}
        
        link = data['link']
        link += token
        msg = Message(sender = "gabriel.lima.moura@poli.ufrj.br",
                      recipients = [user.email],
                      subject = 'Pedido de Mudança de Senha',
                      html = render_template('password_recovery.html', name = user.name, link=link))
        mail.send(msg)
        return {}


class PasswordReset(MethodView):                    #/pw/reset/<token>
    def patch(self, token):
        try:
            received_token = decode_token(token)
        except:
            return {'error': 'invalid token'}, 401
        
        schema = PasswordResetSchema()
        data = schema.load(request.json)  
        
        user = User.query.filter_by(user_id = received_token["sub"]).first()

        if not user:
            return {"error":"Invalid User"}, 404

        user.password = data["password"]
        user.save()
        
        return {}, 204
