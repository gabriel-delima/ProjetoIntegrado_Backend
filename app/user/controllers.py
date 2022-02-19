from functools import partial
from flask import request, jsonify, render_template
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_mail import Message
from app.extensions import mail

from app.user.model import User
from app.user.schemas import UserSchema
from app.utils.filters import filters


class ListUsers(MethodView):
    decorators = [jwt_required()]           #/user/all
    def get(self):

        schema = filters.getSchema(
            qs=request.args, 
            schema_cls=UserSchema,
            many = True
            ) 
        users = User.query.all()
        return jsonify(schema.dump(users)), 200


class UserCurrent(MethodView):             #/user/current
    decorators = [jwt_required()]
    
    def get(self):
        schema = filters.getSchema(
            qs=request.args, 
            schema_cls=UserSchema
            )
        user = User.query.get_or_404(get_jwt_identity()) 
        return schema.dump(user), 200



class UserCreate(MethodView):              #/user/create

    def post(self):
        schema = UserSchema()
        data = request.json
        user = schema.load(data)

        user_check = User.query.filter_by(email=data["email"]).first()
        if user_check:
            return {"error" : "Email already in use"}, 401

        user.save()

        msg = Message(sender = "gabriel.lima.moura@poli.ufrj.br",
                      recipients = [user.email],
                      subject = 'Cadastro Realizado',
                      html = render_template('new_user.html', name=user.name))
        mail.send(msg)

        return schema.dump(user), 201



class UserDetails(MethodView):             #/user/<int:id>
    
    decorators = [jwt_required()]

    def get(self,id):
        if get_jwt_identity() != id:
            return {"error": "User not allowed"}, 400
        schema = filters.getSchema(
            qs=request.args,
            schema_cls=UserSchema
        )
        user = User.query.get_or_404(id)
        return schema.dump(user), 200

    def patch(self,id):
        if get_jwt_identity() != id:
            return {"error": "User not allowed"}, 400
        user = User.query.get_or_404(id)
        schema = UserSchema(exclude=['password','email'])
        user = schema.load(request.json, instance = user, partial=True)
        user.save()
        return UserSchema().dump(user)

    def delete(self,id):
        if get_jwt_identity() != id:
            return {"error": "User not allowed"}, 400
        user = User.query.get_or_404(id)
        user.delete(user)
        return {}, 204