'''
created at 2022/02/09.
created by Shinoda Hiroki.

@ this file is ...
  * this table is cross-reference table.
'''

from models.database import db

class ConferenceEquipment(db.Model):
    # テーブル名を指定
    __tablename__ = 'conference_equipments'

    # テーブルのカラムを設計
    conference_equipments_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
    conference_id = db.Column(db.Integer, db.ForeignKey("conferences.conference_id", onupdate='CASCADE', ondelete='CASCADE'))
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.equipment_id", onupdate='CASCADE', ondelete='CASCADE'))
    num = db.Column(db.Integer)

    # リレーションを定義
    equipments = db.relation("Equipment", backref='conference_equipments')
    conferences = db.relation("Conference", backref='conference_equipments')

    def __init__(self, num, conference_id=None, equipment_id=None):
        self.num = num
        self.conference_id = conference_id
        self.equipment_id = equipment_id