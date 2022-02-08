from models.database import db

class ConferenceEquipment(db.Model):
    # テーブル名を指定
    __tablename__ = 'conference_equipments'

    # テーブルのカラムを設計
    conference_equipments_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
    conference_id = db.Column(db.Integer, db.ForeignKey("conferences.conference_id", onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipments.equipment_id", onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

    def __init__(self, conference_id, equipment_id):
        self.conference_id = conference_id
        self.equipment_id = equipment_id