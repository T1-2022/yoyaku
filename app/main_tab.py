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


# ブループリント設定
main_bp = Blueprint('main_tab', __name__, url_prefix='/main')

# メイン画面
@main_bp.route("/", methods=["GET"])
def main_tab():
    if login_required():
        # データベースからユーザー情報を取得
        user = db.session.query(User).filter_by(email=session['user']).first()
        # ユーザー情報を格納
        user_info = {}
        user_info['name'] = user.name # ユーザーネームを格納
        user_info['email'] = user.email # メールアドレスを格納
        user_info['passwd'] = user.passwd # パスワードを格納

        # 予約情報を全取得 <- 部分的に読み込むようにjsを書いた方がよいかも
        reserves = Reserve.query.all()

        return render_template("main_tab.html", user_info=user_info, reserves=reserves)
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
    for reserve in reserves:
        reserve_lists.append(reserve_list(reserve))    

    conference_lists = ["A-000", "A-001", "A-002"]
    return render_template('calendar/calendar_week.html',reserves=reserve_lists, conferences=conference_lists, test=reserveID)

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
    return render_template('calendar/calendar_simple.html',reserves=reserve_lists_simple)

# 予約ページ
@main_bp.route("/reserve")
def reserve_page():
    return render_template('reserve.html')

# 会議室詳細ページ
@main_bp.route("/room")
def room_page():
    return render_template('room.html')

# ユーザー情報
@main_bp.route("/user_info")
def user_info():
    # データベースからユーザー情報を取得
    user = db.session.query(User).filter_by(email=session['user']).first()
    # ユーザー情報を格納
    user_info = {}
    user_info['name'] = user.name  # ユーザーネームを格納
    user_info['email'] = user.email  # メールアドレスを格納
    user_info['passwd'] = user.passwd  # パスワードを格納
    # 予約情報を全取得 <- 部分的に読み込むようにjsを書いた方がよいかも
    reserves = Reserve.query.all()
    return render_template('user_info.html', user_info=user_info)

# 予約情報リスト定義
def reserve_list(reserve):
    reserve_data = [reserve.__dict__['id'], reserve.__dict__['user_id'], reserve.__dict__['conference_id'],
                         reserve.__dict__['date'], reserve.__dict__['time'], reserve.__dict__['user_name'],
                         reserve.__dict__['user_email'], reserve.__dict__['purpose'],
                         reserve.__dict__['remarks']]
    return reserve_data
