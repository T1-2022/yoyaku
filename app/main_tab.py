from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import session

from models.Register import Register
from models.database import db
from models.User import User
from models.Reserve import Reserve
from models.Conference import Conference
from login import login_required

# ブループリント設定
main_bp = Blueprint('main_tab', __name__, url_prefix='/main')

# メイン画面
@main_bp.route("/", methods=["GET"])
def main_tab():
    if login_required():
        # データベースからユーザー情報を取得
        register = db.session.query(Register).join(User).filter_by(email=session['user']).first()

        # ユーザー情報を格納
        user_info = {}
        user_info['name'] = register.users.name # ユーザーネームを格納
        user_info['email'] = register.users.email # メールアドレスを格納
        user_info['passwd'] = register.passwd # パスワードを格納

        # 予約情報を全取得 <- 部分的に読み込むようにjsを書いた方がよいかも
        reserves = Reserve.query.all()

        return render_template("main_tab.html", user_info=user_info, reserves=reserves)
    else:
        return redirect(url_for('login.login'))
