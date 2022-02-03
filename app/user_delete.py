from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.User import User
from models.database import db
user_delete_bp = Blueprint('user_delete', __name__, url_prefix='/user_delete')

@user_delete_bp.route('/<user_name>')
def user_delete(user_name):
    if user_name != session['user']:
        user = db.session.query(User).filter_by(name=user_name).first()
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('admin_main.admin_main'))