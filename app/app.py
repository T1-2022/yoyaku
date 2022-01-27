from flask import Flask, render_template
from models import database 

app = Flask(__name__)

app.config.from_pyfile('config.py')

database.init_db(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
