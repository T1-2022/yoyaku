<<<<<<< HEAD
from flask import Flask, render_template, redirect

from models import database
from login import login_bp
=======
from flask import Flask, render_template
from models import database 
from mainview import main_view
from changeview import change_view
>>>>>>> 3929db15e8d64509326a30c69c322dea9a496138

app = Flask(__name__)

# config を設定ファイルから読み込む
app.config.from_object('config.DevelopmentConfig')

# データベースの初期化
database.init_db(app)
app.register_blueprint(login_bp)

# ブルーポイント定義
app.register_blueprint(main_view)
app.register_blueprint(change_view)

@app.route("/")
def home():
    return redirect('login')

if __name__ == '__main__':
    app.run()
