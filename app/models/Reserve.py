'''
created at 2022/01/27.
created by Shinoda Hiroki.

@ this file is ... 
  * table name    : reserves
  * id            : int       , nullable=False, primary_key, autoincrement
  * user_id       : string(20), nullable=False, foreignkey("users.id")
  * conference_id : int       , nullable=False, foreignkey("conferences.id")
  * date          : string(30), nullable=False 
  * time          : string(30), nullable=False
  * user_name     : String(20)
  * user_email    : String(50)
  * purpose       : String(100)
  * remakes       : String(100)

  * user is relation to "User"
  * conference is relation to "Conference"
'''

from models.database import db

class Reserve(db.Model):
    # テーブル名の設定
    __tablename__ = 'reserves'

    # テーブルのカラムを設定
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
    user_id = db.Column(db.String(20), db.ForeignKey("users.id"),  nullable=False) # 外部キー
    conference_id = db.Column(db.Integer, db.ForeignKey("conferences.id"), nullable=False) # 外部キー
    date = db.Column(db.String(30), nullable=False)
    time = db.Column(db.String(30), nullable=False)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(50))
    purpose = db.Column(db.String(100))
    remarks = db.Column(db.String(100))

    # 他テーブルとのリレーションを設定
    user = db.relationship("User")
    conference = db.relationship("Conference")