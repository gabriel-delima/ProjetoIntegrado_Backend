
from os import environ

class Config:
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = "postgresql://nkkewfncodswso:a6056423095bbc02133ab5aa8f69fa9d562d6d9fa5044767254d7e687ccc4a7c@ec2-18-234-17-166.compute-1.amazonaws.com:5432/dei91gqsuri2du"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = environ.get('MAIL_PORT')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    SECRET_KEY = environ.get('SECRET_KEY')
    JWT_SECRET_KEY = environ.get('SECRET_KEY')