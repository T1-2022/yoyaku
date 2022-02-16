import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.Register import Register
from models.User import User
from models.database import db
from login import login_required

admin_main_bp = Blueprint('admin_main', __name__, url_prefix='/admin_main')

@admin_main_bp.route('/')
def admin_main():
    if login_required():

        registers = Register.query.all()
        return render_template('main_admin.html',registers=registers)
    else:
        return redirect(url_for('login.login'))
