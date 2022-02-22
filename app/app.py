from datetime import timedelta

from flask import Flask
from flask import render_template,session
from flask import redirect

from admin_user_add import user_add_bp
from admin_main import admin_main_bp
from admin_eq import admin_eq_bp
from admin_room import admin_room_bp
from eq_delete import eq_delete_bp
from room_delete import room_delete_bp
from reserves import reserves_bp
from user_delete import user_delete_bp
from models.User import User
from models import database
from login import login_bp
from main_tab import main_bp

app = Flask(__name__)

# config を設定ファイルから読み込む
app.config.from_object('config.DevelopmentConfig')

# データベースの初期化
database.init_db(app)

# ブループリント定義
app.register_blueprint(main_bp)
app.register_blueprint(login_bp)
app.register_blueprint(user_add_bp)
app.register_blueprint(admin_main_bp)
app.register_blueprint(user_delete_bp)
app.register_blueprint(reserves_bp)
app.register_blueprint(admin_room_bp)
app.register_blueprint(admin_eq_bp)
app.register_blueprint(room_delete_bp)
app.register_blueprint(eq_delete_bp)
app.secret_key = 'user'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return redirect('login')

if __name__ == '__main__':
    app.run()
