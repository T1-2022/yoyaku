'''
created at 2022/01/27.
updated at 2022/02/09.
created by Shinoda Hiroki.

@ this file is ...
  * class named User is User table. 
  * table name : users
  * user_id         : int       , nullable=False, primary_key, autoincrement
  * name       : string(20), nullable=False, unique
  * email      : string(50), nullable=False, unique

  * reserves is relation to "Reserve"
  * registers is relation to "Register"
'''

from models.database import db

class User(db.Model):
    # テーブル名を指定
    __tablename__ = 'users'

    # テーブルのカラムを設計
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    # リレーションを定義
    registers = db.relationship("Register", uselist=False, back_populates='users',cascade='all, delete')
    reserves = db.relationship("Reserve", uselist=True, back_populates='users', cascade='all, delete-orphan')

    # autoincrementであるid以外の値を引数として設定
    def __init__(self, name, email):
      self.name = name
      self.email = email