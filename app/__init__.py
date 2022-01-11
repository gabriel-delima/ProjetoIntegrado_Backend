from flask import Flask
from app.config import Config
from app.extensions import db, migrate, ma, jwt, mail, cors

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    ma.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    cors.init_app(app, resources = {r"/*":{"origins":"*"}})

    return app