#from flask import Flask, render_template
#from project.app.models.database import init_db

# 本番環境に向けてメインファイルの構成を変更
#app = Flask(__name__)


#@app.route("/")
#def home():
#    return render_template("index.html")

from flask import Flask
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
