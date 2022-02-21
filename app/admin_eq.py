import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.database import db
from models.Equipment import Equipment

admin_eq_bp = Blueprint('admin_eq', __name__, url_prefix='/admin_eq')

@admin_eq_bp.route('/', methods=["GET", "POST"])
def admin_eq():
    if request.method == "POST":
        if request.form.get('update') != None:
            print("更新")
            subject_name = request.form['update']
            name = request.form['Name']
            equipment = db.session.query(Equipment).filter_by(name=subject_name).first()
            print(1,subject_name)

            if db.session.query(Equipment).filter_by(name=name).first() == None:
                equipment.name = name
                db.session.add(equipment)
                db.session.commit()

            else:
                equipments = Equipment.query.all()
                return render_template('admin_eq.html', equipments=equipments, error=True)

        else:
            print("追加")
            name = request.form['Name']
            equipment = db.session.query(Equipment).filter_by(name=name).first()

            if equipment != None:
                equipments = Equipment.query.all()
                return render_template('admin_eq.html', equipments=equipments, error=True)
            else:
                equipments = Equipment(name)
                db.session.add(equipments)
                db.session.commit()

    equipments = Equipment.query.all()
    return render_template('admin_eq.html', equipments=equipments,error=False)