import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.Register import Register
from models.User import User
from models.database import db

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/', methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            attempted_email = request.form['email']
            attempted_password = request.form['password']

            register = db.session.query(Register).join(User).filter_by(email=attempted_email).first()

            if register != None and attempted_password == register.__dict__['passwd']:
                    session['user'] = register.users.__dict__['email']
                    session['flag'] = True

                    #if register.__dict__['admin'] == 1:
                    #    return redirect(url_for('admin_main.admin_main'))

                    return redirect(url_for('main_tab.main_tab'))

            else:
                print('invalid credentials')
                session['flag'] = False

        return render_template('index.html')

    except Exception as e:
        return render_template('error.html')

login_bp.secret_key = os.urandom(24)

def login_required():
    if "flag" in session and session["flag"]:
        return True
    else:
        return False
