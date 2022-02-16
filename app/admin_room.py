import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.Conference import Conference
from models.Register import Register
from models.User import User
from models.database import db

admin_room_bp = Blueprint('admin_room', __name__, url_prefix='/admin_room')

@admin_room_bp.route('/', methods=["GET", "POST"])
def admin_room():
    conferences = Conference.query.all()
    return render_template('room.html', conferences)