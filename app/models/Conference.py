from models.database import db

class Conference(db.Model):
    __tablename__ = 'conferences'

    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    capacity = db.Column(db.Integer)
    equipment = db.Column(db.String(30))
    fhoto_id = db.Column(db.Integer, unique=True)
    remarks = db.Column(db.String(100))

    reserve = db.relationship("Reserve")