'''
created at 2022/01/27.
created by Shinoda Hiroki.

@ this file is ... 
  * Define database.
  * Initialize database.
  * Cooperation between db and app. 
  * Cooperation migration.
  * Read tables. 
'''
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

# SQLAlchemyによってdbをインスタンス化
db = SQLAlchemy()

# データベースの初期化
def init_db(app):
    # データベースとアプリケーションの連携
    db.init_app(app)
    # データベースをマイグレーションで管理
    # データベースとアプリケーションをマイグレーションと連携
    Migrate(app, db)

# 作成したテーブル（クラス）を読み込み
from models import User, Conference, Reserve