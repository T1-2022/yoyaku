import os
from flask import render_template, request, session, Blueprint

login_bp = Blueprint('login', __name__, url_prefix='/login')


@login_bp.route('/', methods=["GET", "POST"])
def login():
    try:
        print("login")
        error = ''
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            if attempted_username == 'admin' and attempted_password == os.environ['USER_PASSWORD']:
                session['logged_in'] = True
                session['username'] = request.form['username']
                return render_template('main.html')

            else:
                print('invalid credentials')
                error = 'Invalid credentials. Please, try again.'

        return render_template('login.html', error=error)



    except Exception as e:
        return render_template('login.html', error=str(e))


login_bp.secret_key = os.urandom(24)

