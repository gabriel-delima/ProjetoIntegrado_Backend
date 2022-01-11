from app.extensions import ma
from app.user.model import User

class UserSchema( ma.SQLAlchemySchema):

    class Meta:
        model = User
        load_instance = True
        ordered = True

    user_id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    last_name = ma.String(required=True)
    email = ma.Email(required=True)
    password = ma.String(load_only=True, required=True)

    create_time = ma.DateTime(dump_only=True)
    update_time = ma.DateTime(dump_only=True)