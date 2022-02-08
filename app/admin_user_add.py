import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.User import User
from models.database import db

user_add_bp = Blueprint('admin_user_add', __name__, url_prefix='/admin_user_add')

@user_add_bp.route('/', methods=["GET", "POST"])
def admin_user_add():
    try:
        if request.method == "POST":
            attempted_email = request.form['email']
            attempted_name = request.form['Name']
            attempted_password = request.form['password']

            if  request.form.get('admin')!= 'on':
                attempted_admin = False

            else:
                attempted_admin = True

            user_email = db.session.query(User).filter_by(email=attempted_email).first()

            if user_email == None:
                user = User(name=attempted_name, email=attempted_email, passwd=attempted_password, admin=attempted_admin)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('admin_main.admin_main'))

            else:
                print('invalid credentials')

        return render_template('admin_user_add.html')



    except Exception as e:
        return render_template('error.html')
