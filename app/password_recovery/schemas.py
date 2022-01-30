from app.extensions import ma

class PasswordEmailSchema(ma.Schema):
    email = ma.Email(required=True)
    link = ma.String(required=True)

class PasswordResetSchema(ma.Schema):
    password = ma.String(load_only=True, required=True)
