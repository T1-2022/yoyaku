from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    Migrate(app, db)

# 作成したテーブル（クラス）を読み込み
from models import User, Conference, Reserve