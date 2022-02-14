from datetime import datetime

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import session

from models.Register import Register
from models.database import db
from models.User import User
from models.Reserve import Reserve
from models.Conference import Conference
from login import login_required

reserves_bp = Blueprint('reserves', __name__, url_prefix='/reserves')

# メイン画面
@reserves_bp.route("/",methods=["GET", "POST"])
def reserves():
    if request.method == "POST":
        start_time= request.form['starttime']
        end_time =request.form['endtime']

        if end_time < start_time:
           conferences = Conference.query.all()
           return render_template('reserve.html',conferences = conferences)

        register = db.session.query(Register).join(User).filter_by(email=session['user']).first()
        user_name = request.form['name']
        user_email = request.form['email']


        user_conference = request.form.get('conference')
        print(1)
        print(user_conference)
        reserve_date = datetime.strptime(request.form['date'],'%Y-%m-%d').date()

        reserve_date = "{0:%Y/%m/%d}".format(reserve_date)

        user_purpose = request.form.get('purpose')
        user_remarks = request.form['remarks']

        reserve = db.session.query(Reserve).filter(
            (Reserve.conference_id == user_conference) & (Reserve.date == reserve_date) & (end_time < Reserve.endtime) & (
                        start_time > Reserve.starttime)).all()

        if reserve != None:
            conferences = Conference.query.all()
            return render_template('reserve.html', conferences=conferences)


        user = db.session.query(User).filter_by(email=user_email).first()
        add_reserve = Reserve(register.register_id, user_conference, str(reserve_date),
                              str(start_time), str(end_time), user_purpose, user_remarks)
        if user != None:

            add_reserve.users = user

        else:
            add_reserve.users = User(user_name,user_email)


        db.session.add(add_reserve)
        db.session.commit()

        #return redirect(url_for('main_tab.main_tab'))

    conferences = Conference.query.all()

    return render_template('reserve.html',conferences = conferences)