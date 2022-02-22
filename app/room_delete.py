import os

from flask import Blueprint, redirect, url_for

from models.Conference import Conference
from models.Equipment import Equipment
from models.database import db
from models.ConferenceEquipment import ConferenceEquipment

room_delete_bp = Blueprint('room_delete', __name__, url_prefix='/room_delete')

@room_delete_bp.route('/<name>', methods=["GET", "POST"])
def room_delete(name):
    print("削除")
    conference = db.session.query(Conference).filter_by(name=name).first()
    conference_equipments = db.session.query(ConferenceEquipment).filter_by(conference_id=conference.conference_id).all()
    for conference_equipment in conference_equipments:
        db.session.delete(conference_equipment)

    if os.path.isfile('app/static/img/' + conference.photo_id+'.jpg'):
        os.remove('app/static/img/'  + conference.photo_id+'.jpg')

    print(conference_equipments)

    db.session.delete(conference)
    db.session.commit()

    return redirect(url_for('admin_room.admin_room'))
