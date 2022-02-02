import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.User import User
from models.database import db

user_add_bp = Blueprint('admin_user_add', __name__, url_prefix='/admin_user_add')

@user_add_bp.route('/', methods=["GET", "POST"])
def admin_user_add():
    try:
        if request.method == "POST":

            attempted_name = request.form['name']
            attempted_email = request.form['email']
            attempted_password = request.form['password']

            user_email = db.session.query(User).filter_by(email=attempted_email).first()
            user_name = db.session.query(User).filter_by(name=attempted_name).first()

            if user_email == None and user_name == None:
                user = User(name=attempted_name, email=attempted_email, passwd=attempted_password, admin=False)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login.login'))

            else:
                print('invalid credentials')

        return render_template('admin_user_add.html')



    except Exception as e:
        return render_template('error.html')
