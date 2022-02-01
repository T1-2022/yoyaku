from datetime import timedelta

from flask import Flask
from flask import render_template,session
from flask import redirect
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

app.secret_key = 'user'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return redirect('login')

if __name__ == '__main__':
    app.run()
