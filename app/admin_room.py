import os

from flask import render_template, request, redirect, url_for, Blueprint, Flask, session

from models.ConferenceEquipment import ConferenceEquipment
from models.Conference import Conference
from models.Equipment import Equipment
from models.Register import Register
from models.User import User
from models.database import db

from werkzeug.utils import secure_filename
from flask import send_from_directory

admin_room_bp = Blueprint('admin_room', __name__, url_prefix='/admin_room')

@admin_room_bp.route('/', methods=["GET", "POST"])
def admin_room():
    conferences = Conference.query.all()
    equipments = Equipment.query.all()

    if request.method == "POST":
        if request.form.get('conference'):
            print("更新")
            name = request.form['Name']
            subject_name = request.form['conference']
            capacity = request.form['Capacity']
            conference = db.session.query(Conference).filter_by(name=subject_name).first()

            #備品の数の変更処理
            for equipment in equipments:
                num = request.form.get('equipment'+str(equipment.equipment_id))
                #備品数に数値が入っている場合の処理
                if num and int(num)!= 0:
                    conference_equipment = db.session.query(ConferenceEquipment).filter(
                        (ConferenceEquipment.conference_id==conference.conference_id) &
                        (ConferenceEquipment.equipment_id == equipment.equipment_id)
                    ).first()

                    #会議室に登録されている備品の数の変更
                    if conference_equipment != None:
                        conference_equipment.num = num
                        db.session.add(conference_equipment)
                        db.session.commit()

                    # 会議室に登録されていない備品の数の変更
                    else:
                        conference_equipments = ConferenceEquipment(num,conference.conference_id,equipment.equipment_id)
                        db.session.add(conference_equipments)
                        db.session.commit()

                #備品数が入力されなかった時の処理
                else:
                    conference_equipment = db.session.query(ConferenceEquipment).filter(
                        (ConferenceEquipment.conference_id == conference.conference_id) &
                        (ConferenceEquipment.equipment_id == equipment.equipment_id)
                    ).first()

                    if conference_equipment != None:
                        db.session.delete(conference_equipment)
                        db.session.commit()

            if name != subject_name and db.session.query(Conference).filter_by(name=subject_name).first() == None:
                conference.name = name
                conference.capacity = capacity

                db.session.add(conference)
                db.session.commit()

            elif name == subject_name:
                conference.capacity = capacity
                db.session.add(conference)
                db.session.commit()

            else:
                print("名前")
                conferences = Conference.query.all()
                equipments = Equipment.query.all()
                return render_template('admin_room.html', conferences=conferences, equipments=equipments, error=True)

            if 'file' in request.files['Photo']:
                file = request.files['Photo']
                print(file.filename)

        else:
            name = request.form['Name']
            capacity = request.form['Capacity']
            Photo = request.form['Photo']
            conference = db.session.query(Conference).filter_by(name=name).first()
            print(name,capacity,Photo,conference)
            if conference == None:
                conferences = Conference(name,capacity,Photo,name)
                db.session.add(conferences)
                db.session.commit()
                for equipment in equipments:
                    num = request.form.get('equipment' + str(equipment.equipment_id))
                    print("num:",num)
                    if num and int(num) != 0:
                        conference_equipments = ConferenceEquipment(num, conferences.conference_id,
                                                                    equipment.equipment_id)
                        db.session.add(conference_equipments)
                        db.session.commit()
                    else:
                        conferences = Conference.query.all()
                        equipments = Equipment.query.all()
                        return render_template('admin_room.html', conferences=conferences, equipments=equipments,error=True)
            else:
                conferences = Conference.query.all()
                equipments = Equipment.query.all()
                return render_template('admin_room.html', conferences=conferences, equipments=equipments,error=True)

    conferences = Conference.query.all()
    equipments = Equipment.query.all()
    return render_template('admin_room.html', conferences=conferences,equipments=equipments,error = False)



