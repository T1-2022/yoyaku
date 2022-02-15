from models.database import db
from models.User import User
from models.Conference import Conference
from models.Reserve import Reserve
from models.Register import Register
from models.Equipment import Equipment
from models.ConferenceEquipment import ConferenceEquipment

def reserve():
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email='tarou@example.com').first()
        register = db.session.query(Register).filter_by(user_id=user.user_id).first()
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        reserve = Reserve(register.register_id, conference.conference_id, '2022/02/08', '13:00', '16:00', '授業', '特になし', user.user_id)
        db.session.add(reserve)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()
