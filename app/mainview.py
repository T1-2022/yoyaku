from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from models.database import db
from models.User import User 
from models.Reserve import Reserve 
from models.Conference import Conference 

# ブルーポイント設定
main_view = Blueprint('mainview', __name__)

# 予約情報画面
@main_view.route("/book_info", methods=["GET", "POST"])
def book_info():
    # 出力テスト
    if request.method == "POST":
        #user_id = request.form.get("user_id")
        conference_id = request.form.get("conference_id")
        date = request.form.get("date")
        time = request.form.get("time")
        user_name = request.form.get("user_name")
        user_email = request.form.get("user_email")
        purpose = request.form.get("purpose")
        remarks = request.form.get("remarks")
        
        reserve = Reserve(user_id='test', conference_id=conference_id, date=date, time=time, user_name=user_name, user_email=user_email, purpose=purpose, remarks=remarks)
        db.session.add(reserve)
        db.session.flush()
        db.session.commit()
        
    name = "null"
    reserves = Reserve.query.all()
    return render_template("book_info.html", name=name, reserves=reserves)

# 予約画面
@main_view.route("/booking", methods=["GET", "POST"]) 
def booking():
    name = "null"
    return render_template("booking.html", name=name)

# 会議室詳細画面
@main_view.route("/room", methods=["GET", "POST"])
def room():
    name = "null"
    return render_template("room.html", name=name)

# オンラインヘルプ画面
@main_view.route("/help", methods=["GET", "POST"]) 
def help():
    name = "null"
    return render_template("help.html", name=name)

# ユーザー情報画面
@main_view.route("/user_info", methods=["GET", "POST"]) 
def user_info():
    name = "null"
    mail = "null"
    password = "null"
    return render_template("user_info.html", name=name, mail=mail, password=password)

# 名前変更画面
@main_view.route("/change_name", methods=["GET", "POST"]) 
def change_name():
    name = "null"
    password = "password"
    return render_template("change_name.html", name=name, password=password)

# メールアドレス変更画面
@main_view.route("/change_mail", methods=["GET", "POST"]) 
def change_mail():
    mail = "null"
    password = "password"
    return render_template("change_mail.html", mail=mail, password=password)

# パスワード画面
@main_view.route("/change_password", methods=["GET", "POST"]) 
def change_password():
    password = "password"
    return render_template("change_password.html", password=password)


#ログアウト
#@main_view.route('/')
#@login_required
#def logout():
#    logout_user()
#    return redirect(url_for('.index'))


if __name__ == '__main__':
    main_view.run(debug=True)
