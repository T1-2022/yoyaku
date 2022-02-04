from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from models.database import db
from models.User import User
from models.Reserve import Reserve
from models.Conference import Conference
from login import login_required

# ブループリント設定
main_bp = Blueprint('main_tab', __name__, url_prefix='/main')


# メイン画面
@main_bp.route("/<user_id>", methods=["GET", "POST"])
def main_tab(user_id):
    if login_required():
    # user_idからユーザー名を取得予定
        name=user_id
        reserves = Reserve.query.all()
        return render_template("main_tab.html", name=name, reserves=reserves)
    else:
        return redirect(url_for('login.login'))

#ログアウト
#@main_view.route('/')
#@login_required
#def logout():
#    logout_user()
#    return redirect(url_for('.index'))
