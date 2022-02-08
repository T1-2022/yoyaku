from sqlalchemy.orm import backref
from models.database import db

class Register(db.Model):
    # テーブル名を指定
    __tablename__ = 'registers'

    # テーブルのカラムを設計
    register_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id", onupdate='CASCADE', ondelete='CASCADE'),  nullable=False) # 外部キー
    passwd = db.Column(db.String(30), nullable=False)
    admin = db.Column(db.Boolean, default=False)
    # リレーションを定義
    users = db.relationship("User", uselist=False, back_populates='registers')
    reserves = db.relationship("Reserve", uselist=True, back_populates='registers', cascade='all, delete-orphan')

    # autoincrementであるid以外の値を引数として設定
    def __init__(self, user_id, passwd, admin):
        self.user_id = user_id
        self.passwd = passwd
        self.admin = admin