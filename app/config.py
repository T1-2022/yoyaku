'''
created at 2022/01/27.
created by Shinoda Hiroki.

@ this file is ... 
  * DevelopmentConfig is setting of SQLAlchemy and mode of debug 
'''

import os

# 開発環境でのセッティング（本番環境は別に作成する必要あり）
class DevelopmentConfig:
    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

Config = DevelopmentConfig