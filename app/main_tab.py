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

# ブループリント設定
main_bp = Blueprint('main_tab', __name__, url_prefix='/main')

# メイン画面
@main_bp.route("/<user_id>", methods=["GET", "POST"])
def main_tab(user_id):
    # user_idからユーザー名を取得予定
    name=user_id
    reserves = Reserve.query.all()
    return render_template("main_tab.html", name=name, reserves=reserves, email='tarou@example.com', passwd='passwd')