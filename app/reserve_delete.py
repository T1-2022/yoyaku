from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.Reserve import Reserve
from models.database import db
from models.Register import Register
from models.User import User
from login import login_required

reserve_delete_bp = Blueprint('reserve_delete', __name__, url_prefix='/reserve_delete')

@reserve_delete_bp.route('/<reserve_id>')
def reserve_delete(reserve_id):
    if login_required():
        register = db.session.query(Register).join(User).filter_by(email=session['user']).first()
        reserve = db.session.query(Reserve).filter_by(reserve_id=reserve_id).first()
        if register.admin or reserve.registers.users.email == session['user']:
            db.session.delete(reserve)
            db.session.commit()
        return redirect(url_for('main_tab.calendar_week'))
    return redirect(url_for('login.login'))
