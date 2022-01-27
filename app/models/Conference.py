'''
created at 2022/01/27.
created by Shinoda Hiroki.

@ this file is ... 
  * table name    : conferences
  * id            : int       , nullable=False, primary_key, autoincrement
  * name          : string(20), nullable=False, unique
  * capacity      : int       
  * equipment     : string(30)
  * fhoto_id      : int
  * remakes       : String(100)

  * reserve is relation to "Reserve"
'''

from models.database import db

class Conference(db.Model):
    # テーブルの名前を設定
    __tablename__ = 'conferences'
    
    # テーブルのカラムを設定
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    capacity = db.Column(db.Integer)
    equipment = db.Column(db.String(30))
    fhoto_id = db.Column(db.Integer, unique=True)
    remarks = db.Column(db.String(100))

    # 予約テーブルとのリレーションを作成
    reserve = db.relationship("Reserve")