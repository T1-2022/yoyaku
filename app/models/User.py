'''
created at 2022/01/27.
created by Shinoda Hiroki.

@ this file is ...
  * class named User is User table. 
  * table name : users
  * id         : int       , nullable=False, primary_key, autoincrement
  * name       : string(20), nullable=False, unique
  * email      : string(50), nullable=False, unique
  * passwd     : string(30), nullable=False 
  * admin      : bool      , default='0'

  * reserve is relation to "Reserve"
'''

from models.database import db

class User(db.Model):
    # テーブル名を指定
    __tablename__ = 'users'

    # テーブルのカラムを設計
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
    name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    passwd = db.Column(db.String(30), nullable=False)
    admin = db.Column(db.Boolean, default='0')
    # 外部キーとして連携されるテーブルの設定
    reserve = db.relationship('Reserve')
    