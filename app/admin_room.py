import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.Conference import Conference
from models.Equipment import Equipment
from models.Register import Register
from models.User import User
from models.database import db

admin_room_bp = Blueprint('admin_room', __name__, url_prefix='/admin_room')

@admin_room_bp.route('/', methods=["GET", "POST"])
def admin_room():
    conferences = Conference.query.all()
    equipments = Equipment.query.all()
    for conference in conferences:
        for equipment in conference.conference_equipments:
            num = equipment.num  # 備品数
            name = equipment.equipments.name  # 備品名
            print(name, num)
    return render_template('admin_room.html', conferences=conferences, equipments=equipments)