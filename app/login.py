import os
from datetime import timedelta

from flask import render_template, request, Blueprint, Flask, session

from models.User import User
from models.database import db

login_bp = Blueprint('login', __name__, url_prefix='/login')

@login_bp.route('/', methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":

            attempted_email = request.form['email']
            attempted_password = request.form['password']
            user_db = db.session.query(User).filter_by(email=attempted_email).first()
            print(session["user"])

            if user_db != None and attempted_password == user_db.__dict__['passwd']:
                session["user"] = user_db.__dict__['name']  # セッションでユーザー名を格納
                if user_db.__dict__['admin'] == 1:
                    return render_template('admin.html')#管理者画面への移行

                return render_template('main.html')#メイン画面への移行

            else:
                print('invalid credentials')

        return render_template('index.html')



    except Exception as e:
        return render_template('error.html')#エラー処理


login_bp.secret_key = os.urandom(24)

