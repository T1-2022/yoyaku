from flask import Blueprint, redirect, url_for

from models.Conference import Conference
from models.Equipment import Equipment
from models.database import db

room_delete_bp = Blueprint('room_delete', __name__, url_prefix='/room_delete')

@room_delete_bp.route('/<name>', methods=["GET", "POST"])
def room_delete(name):
    print("削除")
    conference = db.session.query(Conference).filter_by(name=name).first()
    db.session.delete(conference)
    db.session.commit()

    return redirect(url_for('admin_room.admin_room'))
