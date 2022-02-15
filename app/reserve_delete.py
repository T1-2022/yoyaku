from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.Reserve import Reserve
from models.database import db


reserve_delete_bp = Blueprint('reserve_delete', __name__, url_prefix='/reserve_delete')

@reserve_delete_bp.route('/<reserve_id>')
def reserve_delete(reserve_id):
    reserve = db.session.query(Reserve).filter_by(name=reserve_id).first()
    db.session.delete(reserve)
    db.session.commit()

    return redirect(url_for('main_tab.calendar_week'))
