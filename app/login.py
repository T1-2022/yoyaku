import os

from flask import render_template, request, Blueprint, Flask

from models import User
from models.database import db

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/', methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']
            print(1)
            print(db.session.query(User).filter_by(name='shinoda').first())



            if attempted_username == 'admin' and attempted_password == 'aaa':

                    return render_template('main.html')

            else:
                print('invalid credentials')

        return render_template('index.html')



    except Exception as e:
        return render_template('error.html')


login_bp.secret_key = os.urandom(24)

