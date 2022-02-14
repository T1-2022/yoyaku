from datetime import datetime

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
@main_bp.route("/week", methods=["GET", "POST"])
def calendar_week():
    if request.method == "POST":
        reserveID = request.form['reserveID']
    else:
        reserveID = "null"

    reserves = Reserve.query.all()
    reserve_lists=[]
    conferences = Conference.query.all()
    conference_lists=[]

    for conference in conferences:
        conference_lists.append(conference.name)

    print(conference_lists)
    #print(1,request.form['test'])
    for reserve in reserves:
        reserve_lists.append(reserve_list(reserve))

    return render_template('calendar/calendar_week.html',reserves=reserve_lists,conferences=conference_lists, test=reserveID)

# 日表示カレンダー
@main_bp.route("/day")
def calendar_day():
    return render_template('calendar/calendar_day.html')

# 簡易表示カレンダー
@main_bp.route("/simple")
def calendar_simple():
    reserves = Reserve.query.all()
    reserve_lists_simple = []
    for reserve in reserves:
        reserve_lists_simple.append(reserve_list(reserve))

    reserve_lists_simple=sorted(reserve_lists_simple,key=lambda x: (x[4],x[5]))
    #sorted(reserve_lists_simple, key=lambda x: x[5])
    for i in reserve_lists_simple:
        print(i)

    return render_template('calendar/calendar_simple.html', reserves=reserve_lists_simple)

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
    # id, user_id, conf_id, register_name, date, starttime, endtime, user_name, user_email, purpose, remarks

    reserve_data = [reserve.reserve_id, reserve.user_id, reserve.conference_id,
                    reserve.registers.users.name,reserve.date,
                    reserve.starttime, reserve.endtime,reserve.users.name,
                    reserve.users.email,reserve.purpose,reserve.remarks]

    return reserve_data