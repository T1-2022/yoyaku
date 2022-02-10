'''
created at 2022/01/27.
updated at 2022/02/09.
created by Shinoda Hiroki.

@ this file is ... 
  * table name    : conferences
  * id            : int       , nullable=False, primary_key, autoincrement
  * name          : string(20), nullable=False, unique
  * capacity      : int       
  * fhoto_id      : int
  * remarks       : String(100)

  * reserves is relation to "Reserve"
  * equipments is relation to "Equipment"
'''

from models.database import db

class Conference(db.Model):
  # テーブルの名前を設定
  __tablename__ = 'conferences'

  # テーブルのカラムを設定
  conference_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) # 主キー
  name = db.Column(db.String(20), nullable=False, unique=True)
  capacity = db.Column(db.Integer)
  fhoto_id = db.Column(db.Integer, unique=True)
  remarks = db.Column(db.String(100))

  equipments = db.relationship("Equipment", 
                                secondary='conference_equipments',
                                uselist=True,
                                back_populates='conferences',
                                order_by='Equipment.equipment_id')
  reserves = db.relationship("Reserve", uselist=True, back_populates='conferences', cascade='all, delete-orphan')

  def __init__(self, name, capacity, fhoto_id, remarks):
      self.name = name
      self.capacity = capacity
      self.fhoto_id = fhoto_id
      self.remarks = remarks