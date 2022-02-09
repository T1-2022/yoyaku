'''
created at 2022/01/27.
updated at 2022/02/09.
created by Shinoda Hiroki.

@ this file is ... 
  * table name    : reserves
  * reserve_id    : int       , nullable=False, primary_key, autoincrement
  * register_id   : int       , nullable=False, foreignkey("registers.register_id")
  * conference_id : int       , nullable=False, foreignkey("conferences.conference_id")
  * date          : string(30), nullable=False 
  * time          : string(30), nullable=False
  * user_id       : int       , nullable=False, foreignkey("users.user_id")
  * purpose       : String(10), nullable=False
  * remarks       : String(100)

  * registers is relation to "Register"
  * users is relation to "User"
  * conferences is relation to "Conference"
'''

from models.database import db

class Reserve(db.Model):
  # テーブル名の設定
  __tablename__ = 'reserves'

  # テーブルのカラムを設定
  reserve_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
  register_id = db.Column(db.Integer, db.ForeignKey("registers.register_id", onupdate='CASCADE', ondelete='CASCADE'),  nullable=False) # 外部キー
  conference_id = db.Column(db.Integer, db.ForeignKey("conferences.conference_id", onupdate='CASCADE', ondelete='CASCADE'), nullable=False) # 外部キー
  date = db.Column(db.String(30), nullable=False)
  time = db.Column(db.String(30), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey("users.user_id", onupdate='CASCADE', ondelete='CASCADE')) # 外部キー
  purpose = db.Column(db.String(10), nullable=False)
  remarks = db.Column(db.String(100))

  # 各テーブルへのリレーションを設定
  registers = db.relationship("Register", uselist=False, back_populates='reserves')
  conferences = db.relationship("Conference", uselist=False, back_populates='reserves')
  users = db.relationship("User", uselist=False, back_populates='reserves')
  
  def __init__(self, register_id, conference_id, date, time, purpose, remarks, user_id=None):
    self.register_id = register_id
    self.conference_id = conference_id
    self.date = date
    self.time = time
    self.user_id = user_id
    self.purpose = purpose
    self.remarks = remarks