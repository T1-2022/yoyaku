import json
from datetime import datetime, timedelta

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

#非同期用グローバル変数
week_day = None
day_time = None

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

@main_bp.route('/week_Ajax_POST', methods=['POST'])
def week_Ajax_POST():
    global week_day
    if request.method == "POST":
        week_day = request.json

    return week_day

@main_bp.route('/week_Ajax_GET', methods=['GET'])
def week_Ajax_GET():
    global week_day
    reserve_lists=[]
    if(week_day != None):
        Sunday = datetime.strptime(week_day,'%Y/%m/%d').date()
        Saturday = Sunday+ timedelta(days=6)
        Sunday="{0:%Y/%m/%d}".format(Sunday)
        Saturday="{0:%Y/%m/%d}".format(Saturday)

        print(Sunday)
        reserves = db.session.query(Reserve).filter(
            (str(Sunday) <= Reserve.date)
            & (str(Saturday) >= Reserve.date)).all()

        for reserve in reserves:
            reserve_lists.append(reserve_list(reserve))

        return json.dumps(reserve_lists)

    return json.dumps(None)

# 日表示カレンダー
@main_bp.route("/day",methods=["GET"])
def calendar_day():
    if request.method == "POST":
        reserveID = request.form['reserveID']
    else:
        reserveID = "null"

    reserves = Reserve.query.all()
    reserve_lists=[]
    for reserve in reserves:
        reserve_lists.append(reserve_list(reserve))

    conferences = Conference.query.all()
    conference_lists = []

    for conference in conferences:
        data = [conference.conference_id, conference.name]
        conference_lists.append(data)


    return render_template('calendar/calendar_day.html',reserves=reserve_lists, conferences=conference_lists)

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

    conferences = Conference.query.all()
    conference_lists = []

    for conference in conferences:
        conference_lists.append(conference.name)

    return render_template('calendar/calendar_simple.html', reserves=reserve_lists_simple,conferences=conference_lists)

# 予約ページ
@main_bp.route("/reserve")
def reserve_page():
    return redirect(url_for('reserves.reserves'))

# 会議室詳細ページ
@main_bp.route("/room")
def room_page():
    conferences = Conference.query.all()
    return render_template('room.html',conferences=conferences)

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

