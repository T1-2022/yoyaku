from flask import Flask, render_template
from mainview import main_view

app = Flask(__name__)

app.register_blueprint(main_view)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
