from app.extensions import db
from app.models import BaseModel
import bcrypt

class User(BaseModel):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.LargeBinary(128), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")
    
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt())

    def verify_password(self, password) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash)