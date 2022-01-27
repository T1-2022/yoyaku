'''
created at 2022/01/27
created by Shinoda Hiroki

table named reserve in database


'''

from models.database import db

class Reserve(db.Model):
    __tablename__ = 'reserves'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20), db.ForeignKey("users.id"),  nullable=False) # 外部キー
    conference_id = db.Column(db.Integer, db.ForeignKey("conferences.id"), nullable=False) # 外部キー
    date = db.Column(db.String(30), nullable=False)
    time = db.Column(db.String(30), nullable=False)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(50))
    purpose = db.Column(db.String(100))
    remarks = db.Column(db.String(100))

    user = db.relationship("User")
    conference = db.relationship("Conference")