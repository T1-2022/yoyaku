from models.database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    passwd = db.Column(db.String(30), nullable=False)
    admin = db.Column(db.Boolean, default="0")

    reserve = db.relationship("Reserve")
    