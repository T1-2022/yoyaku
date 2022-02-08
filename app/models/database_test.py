from models.database import db
from models.User import User
from models.Conference import Conference
from models.Reserve import Reserve
from models.Register import Register
from models.Equipment import Equipment
from models.ConferenceEquipment import ConferenceEquipment

'''
User関連のCRUD関数
'''

# User作成
def add_user():
    db.session.begin()
    try:
        user = User('豊橋太郎', 'tarou@example.com')
        db.session.add(user)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# User削除
def delete_user():
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email='tarou@example.com').first()
        db.session.delete(user)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# User更新
def update_user():
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email='tarou@example.com').first()
        user.email = 'tarou.toyohasi@example.com'
        db.session.add(user)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

'''
Register関連のCRUD関数
'''

# Register 追加
def add_register():
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email='tarou@example.com').first()
        register = Register(user.user_id, 'passwd', False)
        db.session.add(register)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# Register 読み込み
def read_register():
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email='tarou@example.com').first()
        register = db.session.query(Register).filter_by(user_id=user.user_id).first()
        print("[debug] : {}".format(register.users))
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# Register 削除
def delete_register():
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email='tarou@example.com').first()
        register = db.session.query(Register).filter_by(user_id=user.user_id).first()
        db.session.delete(register)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# Register 更新
def update_register():
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email='tarou@example.com').first()
        register = db.session.query(Register).filter_by(user_id=user.user_id).first()
        register.passwd = 'passwd2'
        db.session.add(register)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

'''
Equipment関連のCRUD関数
'''

# Equipment 追加
def add_equipment():
    db.session.begin()
    try:
        equipment = Equipment('プロジェクター')
        db.session.add(equipment)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# Equipment 読み込み
def read_equipment():
    db.session.begin()
    try:
        equipment = db.session.query(Equipment).filter_by(name='プロジェクター').first()
        print("[debug] : {}".format(equipment.conferences))
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# Equipment 削除
def delete_equipment():
    db.session.begin()
    try:
        equipment = db.session.query(Equipment).filter_by(name='プロジェクター').first()
        db.session.delete(equipment)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# Equipment 更新
def update_equipment():
    db.session.begin()
    try:
        equipment = db.session.query(Equipment).filter_by(name='プロジェクター').first()
        equipment.name = 'プリンター'
        db.session.add(equipment)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

'''
Conference関連のCRUD関数
'''

# Conference 追加
def add_conference():
    db.session.begin()
    try:
        conference = Conference('会議室A', 60, 1, '特になし')
        db.session.add(conference)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# Conference 読み込み
def read_conference():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        print("[debug] : {}".format(conference.equipments))
        print("[debug] : {}".format(conference.reserves))
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# Conference 削除
def delete_conference():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        db.session.delete(conference)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# Conference 更新
def update_conference():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        conference.capacity = 80
        db.session.add(conference)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

'''
Reserve 関連のCRUD関数
'''

# Reserve 追加
def add_reserve():
    db.session.begin()
    try:
        reserve = Reserve('会議室A', 60, 1, '特になし')
        db.session.add(reserve)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# Reserve 読み込み
def read_reserve():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        print("[debug] : {}".format(conference.equipments))
        print("[debug] : {}".format(conference.reserves))
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# Reserve 削除
def delete_reserve():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        db.session.delete(conference)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# Reserve 更新
def update_reserve():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        conference.capacity = 80
        db.session.add(conference)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

'''
ConferenceEquipment 関連のCRUD関数
'''

# ConferenceEquipment 追加
def add_conference_equipment():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        equipment = db.session.query(Equipment).filter_by(name='プリンター').first()
        conference_equipment = ConferenceEquipment(conference.conference_id, equipment.equipment_id)
        db.session.add(conference_equipment)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# ConferenceEquipment 読み込み
def read_conference_equipment():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        conference_equipment = db.session.query(ConferenceEquipment).filter_by(conference_id=conference.conference_id).first()
        #print("[debug] : {}".format(conference.equipments))
        #print("[debug] : {}".format(conference.reserves))
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# ConferenceEquipment 削除
def delete_conference_equipment():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        db.session.delete(conference)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

# ConferenceEquipment 更新
def update_conference_equipment():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        conference.capacity = 80
        db.session.add(conference)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.rollback()
        print(e)
    finally:
        db.session.close()

'''
単体テスト

各テーブルへの登録，削除，更新が行えるかテスト
'''

# User テスト
def test_User():
    # ユーザー追加テスト
    print("[test] : add user.")
    add_user()
    # ユーザー削除テスト
    print("[test] : delete user.")
    delete_user()
    # ユーザー情報更新テスト
    print("[test] : update user.")
    add_user()
    update_user()

# Register テスト
def test_Register():
    # 登録者追加テスト
    print("[test] : add register.")
    add_user()
    add_register()
    # 登録者の読み込みテスト
    print("[test] : read register.")
    read_register()
    # 登録者の削除テスト
    print("[test] : delete register.")
    delete_register()
    # 登録者の情報更新テスト
    print("[test] : update register.")
    add_register()
    update_register()

# Equipment テスト
def test_Equipment():
    # 備品追加テスト
    print("[test] : add equipment.")
    add_equipment()
    # 備品の読み込みテスト
    print("[test] : read equipment.")
    read_equipment()
    # 備品の削除テスト
    print("[test] : delete equipment.")
    delete_equipment()
    # 備品の情報更新テスト
    print("[test] : update equipment.")
    add_equipment()
    update_equipment()

# Conference テスト
def test_Conference():
    # 会議室追加テスト
    print("[test] : add conference.")
    add_conference()
    # 会議室の読み込みテスト
    print("[test] : read conference.")
    read_conference()
    # 会議室の削除テスト
    print("[test] : delete conference.")
    delete_conference()
    # 会議室の情報更新テスト
    print("[test] : update conference.")
    add_conference()
    update_conference()