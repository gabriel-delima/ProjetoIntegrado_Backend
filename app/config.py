from os import environ

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///data-dev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    MAIL_SERVER = "smtp.sendgrid.net"
    MAIL_PORT = 587
    MAIL_USERNAME = "apikey"
    MAIL_PASSWORD = "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"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    SECRET_KEY = "sadg5ad6sg54adsg65sa4dg3sd4ag6s54g6ASDASDASFAFsda54g6sa54"
    JWT_SECRET_KEY = "sadg5ad6sg54adsg65sa4dg3sd4ag6s54g6ASDASDASFAFsda54g6sa54"

