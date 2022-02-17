import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.Equipment import Equipment

admin_eq_bp = Blueprint('admin_eq', __name__, url_prefix='/admin_eq')

@admin_eq_bp.route('/', methods=["GET", "POST"])
def admin_eq():
    equipments = Equipment.query.all()
    return render_template('admin_eq.html', equipments=equipments)