from flask import Flask, render_template
from models import database 

app = Flask(__name__)

# config を設定ファイルから読み込む
app.config.from_object('config.DevelopmentConfig')

# データベースの初期化
database.init_db(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
