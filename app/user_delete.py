from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.User import User
from models.database import db
user_delete_bp = Blueprint('user_delete', __name__, url_prefix='/user_delete')

@user_delete_bp.route('/<user_email>')
def user_delete(user_email):
    if user_email != session['user']:
        user = db.session.query(User).filter_by(email=user_email).first()
        db.session.delete(user)
        db.session.commit()


    return redirect(url_for('admin_main.admin_main'))