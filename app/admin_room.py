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

            #名前に変更がある場合の処理
            if name != subject_name:
                if db.session.query(Conference).filter_by(name=name).first() == None:
                    conference.name = name
                    conference.capacity = capacity
                    os.rename('app/static/img/'+str(conference.photo_id)+'.jpg','app/static/img/'+name+'.jpg')
                    conference.photo_id = name
                    db.session.add(conference)
                    db.session.commit()
                    # 変更しようとした名前が既存の名前である場合のエラー処理

                else:
                    print("名前",subject_name,name)
                    conferences = Conference.query.all()
                    equipments = Equipment.query.all()
                    return render_template('admin_room.html', conferences=conferences, equipments=equipments,
                                           error=True)

            # 名前に変更が無い場合の処理
            else:
                conference.capacity = capacity
                db.session.add(conference)
                db.session.commit()



            file = request.files.get('Photo')
            if file != None:
                file = request.files['Photo']
                if name != subject_name:
                    file.filename = name+".jpg"
                    if os.path.isfile('app/static/img/'+file.filename):
                        os.remove('app/static/img/'+file.filename)

                    file.save('app/static/img/' + file.filename)

                else:
                    file.filename = name + ".jpg"
                    if os.path.isfile('app/static/img/'+file.filename):
                        os.remove('app/static/img/'+file.filename)

                    file.save('app/static/img/'+file.filename)

        else:
            print("追加")
            name = request.form['Name']
            capacity = request.form['Capacity']
            conference = db.session.query(Conference).filter_by(name=name).first()

            if conference == None:
                conferences = Conference(name,capacity,name,name)
                db.session.add(conferences)
                db.session.commit()
                for equipment in equipments:
                    num = request.form.get('equipment' + str(equipment.equipment_id))

                    if num and int(num) != 0:
                        conference_equipments = ConferenceEquipment(num, conferences.conference_id,
                                                                    equipment.equipment_id)
                        db.session.add(conference_equipments)
                        db.session.commit()

            else:
                conferences = Conference.query.all()
                equipments = Equipment.query.all()
                return render_template('admin_room.html', conferences=conferences, equipments=equipments,error=True)

            file = request.files.get('Photo')
            if file != None:
                file = request.files['Photo']
                file.filename = name + ".jpg"
                if os.path.isfile('app/static/img/' + file.filename):
                    conferences = Conference.query.all()
                    equipments = Equipment.query.all()
                    return render_template('admin_room.html', conferences=conferences, equipments=equipments,
                                           error=True)

            file.save('app/static/img/' + file.filename)

    conferences = Conference.query.all()
    equipments = Equipment.query.all()
    return render_template('admin_room.html', conferences=conferences,equipments=equipments,error = False)



