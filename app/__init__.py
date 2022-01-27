from flask import Flask

# アプリケーションの作成を行う
# モジュール化したファイルを読み込む
def create_app():
    # インスタンスの作成
    app = Flask(__name__)
    # configファイルから環境変数等を読み込む
    app.config.from_pyfile('config.py')

    # データベースの作成
    from app.model import database as db
    db.init_db(app)

    @app.route("/")
    def home():
        return render_template("index.html")

    return app
