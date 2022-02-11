from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import session
from models.database import db
from models.User import User
from models.Reserve import Reserve
from models.Conference import Conference
from login import login_required

reserves_bp = Blueprint('reserves', __name__, url_prefix='/reserves')

# メイン画面
@reserves_bp.route("/", methods=["GET"])
def reserves():
    return redirect(url_for('reserves'))

