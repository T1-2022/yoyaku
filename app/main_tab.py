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
        user_info['name'] =  register.users.name # ユーザーネームを格納
        user_info['email'] = register.users.email # メールアドレスを格納
        user_info['passwd'] = register.passwd # パスワードを格納

        # 予約情報を全取得 <- 部分的に読み込むようにjsを書いた方がよいかも
        return render_template("main_tab.html", user_info=user_info)

    else:
        return redirect(url_for('login.login'))

# 週表示カレンダー
@main_bp.route("/week")
def calendar_week():
    reserves = Reserve.query.all()
    reserve_lists=[]

    for reserve in reserves:
        reserve_lists.append(reserve_list(reserve))

    return render_template('calendar/calendar_week.html',reserves=reserve_lists)

# 日表示カレンダー
@main_bp.route("/day")
def calendar_day():
    return render_template('calendar/calendar_day.html')

# 簡易表示カレンダー
@main_bp.route("/simple")
def calendar_simple():
    return render_template('calendar/calendar_simple.html')

# 予約ページ
@main_bp.route("/reserve")
def reserve_page():
    return redirect(url_for('reserves.reserves'))

# ユーザー情報
@main_bp.route("/user_info")
def user_info():
    # データベースからユーザー情報を取得
    register = db.session.query(Register).join(User).filter_by(email=session['user']).first()

    # ユーザー情報を格納
    user_info = {}
    user_info['name'] = register.users.name  # ユーザーネームを格納
    user_info['email'] = register.users.email  # メールアドレスを格納
    user_info['passwd'] = register.passwd  # パスワードを格納
    # 予約情報を全取得 <- 部分的に読み込むようにjsを書いた方がよいかも
    reserves = Reserve.query.all()
    return render_template('user_info.html', user_info=user_info)

def reserve_list(reserve):
    # id, user_id, conf_id, date, time, user_name, user_email, purpose, remarks


    reserve_data = [reserve.reserve_id, reserve.user_id, reserve.conference_id,
                    reserve.date, reserve.starttime, reserve.users.name,
                    reserve.users.email,reserve.purpose,reserve.remarks]

    return reserve_data