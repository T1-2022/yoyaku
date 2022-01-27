import os

class DevelopmentConfig:
    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.path.join('sqlite:///', 'app/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


Config = DevelopmentConfig
print("a", Config.SQLALCHEMY_DATABASE_URI)