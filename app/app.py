from flask import Flask, render_template
import database 

# 本番環境に向けてメインファイルの構成を変更
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

database.init_db(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
