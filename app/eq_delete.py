from flask import Blueprint, redirect, url_for

from models.ConferenceEquipment import ConferenceEquipment
from models.Equipment import Equipment
from models.database import db

eq_delete_bp = Blueprint('eq_delete', __name__, url_prefix='/eq_delete')

@eq_delete_bp.route('/<name>', methods=["GET", "POST"])
def eq_delete(name):

    equipment = db.session.query(Equipment).filter_by(name=name).first()
    c_eqs = db.session.query(ConferenceEquipment).filter_by(equipment_id=equipment.equipment_id).all()
    for c_eq in c_eqs:
        db.session.delete(c_eq)

    db.session.commit()
    db.session.delete(equipment)
    db.session.commit()

    return redirect(url_for('admin_eq.admin_eq'))
