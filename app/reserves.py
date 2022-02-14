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
        select_start_hour = request.form.get('select_start_hour')
        select_start_minute = request.form.get('select_start_minute')

        select_end_hour = request.form.get('select_end_hour')
        select_end_minute = request.form.get('select_end_minute')

        if select_end_hour < select_start_hour:
            conferences = Conference.query.all()
            return render_template('reserve.html',conferences = conferences)

        register = db.session.query(Register).join(User).filter_by(email=session['user']).first()

        user_name = request.form['Name']
        user_email = request.form['email']

        user_conference = request.form.get('conference')
        conference = db.session.query(Conference).filter_by(name=user_conference).first()

        select_year = str(request.form.get('select_year'))
        select_month = str(request.form.get('select_month'))
        select_day = str(request.form.get('select_day'))

        reserve_date = datetime.strptime(
            select_year + "-" + select_month + "-" + select_day,
            '%Y-%m-%d').date()

        reserve_date = "{0:%Y/%m/%d}".format(reserve_date)

        start_time = datetime.strptime(
            str(select_start_hour) + ":" + str(select_start_minute),
            '%H:%M').time()

        end_time = datetime.strptime(
            str(select_end_hour) + ":" + str(select_end_minute),
            '%H:%M').time()

        user_purpose = request.form.get('purpose')
        user_remarks = request.form['remarks']

        user = db.session.query(User).filter_by(email=user_email).first()

        if user != None:
            add_reserve = Reserve(register.register_id, conference.conference_id, str(reserve_date), str(start_time),
                                 user_purpose, user_remarks, user.user_id)
            db.session.add(add_reserve)
            db.session.commit()

        else:
            add_reserve = Reserve(register.register_id,conference.conference_id,str(reserve_date),str(start_time),user_purpose,user_remarks)
            add_reserve.users = User(user_name,user_email)

            db.session.add(add_reserve)
            db.session.commit()

        print(user_remarks)

        return redirect(url_for('main_tab.main_tab'))

    conferences = Conference.query.all()
    return render_template('reserve.html',conferences = conferences)