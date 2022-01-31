import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask

from models.User import User
from models.database import db

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/', methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']
            user = db.session.query(User).filter_by(name=attempted_username).first()

            if user != None and attempted_password == user.__dict__['passwd']:
                    if user.__dict__['admin'] == 1:
                        return render_template('admin.html')

                    return redirect(url_for('main_tab.main_tab', user_id=attempted_username))

            else:
                print('invalid credentials')

        return render_template('index.html')



    except Exception as e:
        return render_template('error.html')


login_bp.secret_key = os.urandom(24)

