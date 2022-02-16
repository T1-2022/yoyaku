import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.Register import Register
from models.User import User
from models.database import db
from login import login_required

user_add_bp = Blueprint('admin_user_add', __name__, url_prefix='/admin_user_add')

@user_add_bp.route('/', methods=["GET", "POST"])
def admin_user_add():
    if login_required():
        try:
            if request.method == "POST":
                attempted_email = request.form['email']
                attempted_name = request.form['Name']
                attempted_password = request.form['password']

                if  request.form.get('admin')!= 'on':
                    attempted_admin = False

                else:
                    attempted_admin = True

                user = db.session.query(User).filter_by(email=attempted_email).first()
                register = None

                if user != None:
                    register = db.session.query(Register).filter_by(user_id=user.user_id).first()
                    if register == None:
                        add_register = Register(user_id=user.user_id, passwd=attempted_password, admin=attempted_admin)
                        db.session.add(add_register)
                        db.session.commit()
                        return redirect(url_for('admin_main.admin_main'))

                else:
                    add_register = Register(passwd=attempted_password, admin=attempted_admin)
                    add_register.users = User(name=attempted_name, email=attempted_email, )
                    db.session.add(add_register)
                    db.session.commit()
                    return redirect(url_for('admin_main.admin_main'))




            return render_template('admin_user_add.html')



        except Exception as e:
            return render_template('error.html')
    else:
        return redirect(url_for('login.login'))
