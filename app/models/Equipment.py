from models.database import db

class Equipment(db.Model):
    # テーブル名を指定
    __tablename__ = 'equipments'

    # テーブルのカラムを設計
    equipment_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
    name = db.Column(db.String(30), unique=True, nullable=False)
    #num = db.Column(db.Integer, nullable=False)

    conferences = db.relationship("Conference", 
                                secondary='conference_equipments',
                                uselist=True,
                                back_populates='equipments',
                                order_by='Conference.conference_id',
                                cascade='all, delete')

    def __init__(self, name):
        self.name = name
        #self.num = num