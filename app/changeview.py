from flask import Flask
from flask import render_template
from flask import request
from flask import Blueprint
from models.database import db
from models.User import User 
from models.Reserve import Reserve 
from models.Conference import Conference 

# ブルーポイント設定
change_view = Blueprint('changeview', __name__)

# 名前変更画面
@change_view.route("/change_name", methods=["GET", "POST"]) 
def change_name():
    name = "null"
    password = "password"
    return render_template("change_name.html", name=name, password=password)

# メールアドレス変更画面
@change_view.route("/change_mail", methods=["GET", "POST"]) 
def change_mail():
    mail = "null"
    password = "password"
    return render_template("change_mail.html", mail=mail, password=password)

# パスワード画面
@change_view.route("/change_password", methods=["GET", "POST"]) 
def change_password():
    password = "password"
    return render_template("change_password.html", password=password)

if __name__ == '__main__':
    change_view.run(debug=True)
