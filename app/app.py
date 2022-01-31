from flask import Flask, render_template
from models import database 
from mainview import main_view
from changeview import change_view

app = Flask(__name__)

# config を設定ファイルから読み込む
app.config.from_object('config.DevelopmentConfig')

# データベースの初期化
database.init_db(app)

# ブルーポイント定義
app.register_blueprint(main_view)
app.register_blueprint(change_view)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
