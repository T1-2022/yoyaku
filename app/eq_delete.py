from flask import Blueprint, redirect, url_for


from models.Equipment import Equipment
from models.database import db

eq_delete_bp = Blueprint('eq_delete', __name__, url_prefix='/eq_delete')

@eq_delete_bp.route('/<name>', methods=["GET", "POST"])
def eq_delete(name):
    conference = db.session.query(Equipment).filter_by(name=name).first()
    db.session.delete(conference)
    db.session.commit()

    return redirect(url_for('admin_eq.admin_eq'))
