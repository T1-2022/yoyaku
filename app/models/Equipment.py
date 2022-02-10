'''
created at 2022/02/09.
created by Shinoda Hiroki.

@ this file is ...
  * table name    : equipments
  * equipment_id  : int       , nullable=False, primary_key, autoincrement
  * name          : string(20), nullable=False, unique

  * conferences is relation to "Conference"  
'''

from models.database import db

class Equipment(db.Model):
    # テーブル名を指定
    __tablename__ = 'equipments'

    # テーブルのカラムを設計
    equipment_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
    name = db.Column(db.String(30), unique=True, nullable=False)

    conferences = db.relationship("Conference", 
                                secondary='conference_equipments',
                                uselist=True,
                                back_populates='equipments',
                                order_by='Conference.conference_id')

    def __init__(self, name):
        self.name = name