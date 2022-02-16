'''
    created at 2022/02/09
    created by shinoda hiroki

    @this file is ...
    test cases in database.
'''

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
def add_user(name='豊橋太郎', email='tarou@example.com'):
    db.session.begin()
    try:
        user = User(name, email)
        db.session.add(user)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# User削除
def delete_user(email='tarou@example.com'):
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email=email).first()
        db.session.delete(user)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# User更新
def update_user(old_email='tarou@example.com', new_email='toyohasi.tarou@example.com'):
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email=old_email).first()
        user.email = new_email
        db.session.add(user)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
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
        register = Register('passwd', False, user.user_id)
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
        db.session.rollback()
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
        db.session.rollback()
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
        db.session.rollback()
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
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# Equipment 削除
def delete_equipment(name='プロジェクター'):
    db.session.begin()
    try:
        equipment = db.session.query(Equipment).filter_by(name=name).first()
        db.session.delete(equipment)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
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
        db.session.rollback()
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
        db.session.rollback()
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
        db.session.rollback()
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
        db.session.rollback()
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

# Reserve 読み込み
def read_reserve():
    db.session.begin()
    try:
        reserve = db.session.query(Reserve).filter_by(date='2022/02/08').first()
        print("[debug] : {}".format(reserve.registers))
        print("[debug] : {}".format(reserve.conferences))
        print("[debug] : {}".format(reserve.users))
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# Reserve 削除
def delete_reserve():
    db.session.begin()
    try:
        reserve = db.session.query(Reserve).filter_by(date='2022/02/08').first()
        db.session.delete(reserve)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# Reserve 更新
def update_reserve():
    db.session.begin()
    try:
        reserve = db.session.query(Reserve).filter((Reserve.date=='2022/02/08') & (Reserve.starttime=='13:00')).first()
        #reserve.starttime = '13:00'
        reserve.endtime = '14:40'
        db.session.add(reserve)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# reserve 日付の処理テスト
def get_reserve():
    db.session.begin()
    try:
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('12:00' < Reserve.endtime) & ('13:00' > Reserve.starttime)).all()
        print(reserve)
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('12:00' < Reserve.endtime) & ('14:00' > Reserve.starttime)).all()
        print(reserve)
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('14:00' < Reserve.endtime) & ('15:00' > Reserve.starttime)).all()
        print(reserve)
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('13:30' < Reserve.endtime) & ('14:00' > Reserve.starttime)).all()
        print(reserve)
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('12:00' < Reserve.endtime) & ('15:00' > Reserve.starttime)).all()
        print(reserve)
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# reserve 日付の処理テスト
def get_reserve():
    db.session.begin()
    try:
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('12:00' < Reserve.endtime) & ('13:00' > Reserve.starttime)).all()
        print(reserve)
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('12:00' < Reserve.endtime) & ('14:00' > Reserve.starttime)).all()
        print(reserve)
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('14:00' < Reserve.endtime) & ('15:00' > Reserve.starttime)).all()
        print(reserve)
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('13:30' < Reserve.endtime) & ('14:00' > Reserve.starttime)).all()
        print(reserve)
        reserve = db.session.query(Reserve).filter((Reserve.conference_id == '1') & (Reserve.date == '2022/02/08') & ('12:00' < Reserve.endtime) & ('15:00' > Reserve.starttime)).all()
        print(reserve)
    except Exception as e:
        db.session.rollback()
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
    add_user('豊橋太郎', 'tarou@example.com')
    # ユーザー削除テスト
    print("[test] : delete user.")
    delete_user('tarou@example.com')
    # ユーザー情報更新テスト
    print("[test] : update user.")
    add_user('豊橋太郎', 'tarou@example.com')
    update_user('tarou@example.com', 'toyohasi.tarou@example.com')
    delete_user('toyohasi.tarou@example.com')

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
    delete_register()
    delete_user('tarou@example.com')

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
    delete_equipment('プリンター')

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
    delete_conference()

# Reserve テスト
def test_Reserve():
    # 予約追加テスト
    print("[test] : add reserve.")
    add_reserve()
    # 予約の読み込みテスト
    print("[test] : read reserve.")
    read_reserve()
    # 予約の削除テスト
    print("[test] : delete reserve.")
    delete_reserve()
    # 予約の情報更新テスト
    print("[test] : update reserve.")
    add_reserve()
    update_reserve()
    delete_reserve()


'''
複合テスト

リレーション関係のあるデータベースが更新された際の動作
'''

# RegisterにUserを登録
# 自動的にUserにも追加される
def add_user_in_register():
    db.session.begin()
    try:
        register = Register('passwd', False)
        register.users = User('豊橋花子', 'hanako@example.com')
        db.session.add(register)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# Userを削除した場合Registerも削除される
def delete_user_and_register():
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email='hanako@example.com').first()
        db.session.delete(user)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# Registerを削除した場合Userは削除されない
def delete_register_and_user():
    db.session.begin()
    try:
        user = db.session.query(User).filter_by(email='hanako@example.com').first()
        register = db.session.query(Register).filter_by(user_id=user.user_id).first()
        db.session.delete(register)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# 会議室と備品の結びつけ
def connect_conference_equipment():
    db.session.begin()
    try:
        conference = Conference('会議室A', 60, 1, '特になし')
        conference.equipments.append(Equipment('プロジェクター'))
        db.session.add(conference)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# 会議室を削除した際に備品は削除されない
def delete_conference_without_equipment():
    db.session.begin()
    try:
        conference = db.session.query(Conference).filter_by(name='会議室A').first()
        db.session.delete(conference)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# 備品を削除した際に会議室は削除されない
def delete_equipment_without_conference():
    db.session.begin()
    try:
        equipment = db.session.query(Equipment).filter_by(name='プロジェクター').first()
        db.session.delete(equipment)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    finally:
        db.session.close()

# 予約を削除した際に会議室，予約者，利用者を削除しない
def delete_reserve_without_conference_register_user():
    add_user('豊橋太郎', 'tarou@example.com')
    add_register()
    add_conference()
    add_reserve()
    delete_reserve()

# 会議室を削除した際に予約を削除する
def delete_conference_and_reserve_without_register_user():
    add_user('豊橋太郎', 'tarou@example.com')
    add_register()
    add_conference()
    add_reserve()
    delete_conference()

# 予約者を削除した際に予約を削除する
def delete_register_and_reserve_without_conference_user():
    add_user('豊橋太郎', 'tarou@example.com')
    add_register()
    add_conference()
    add_reserve()
    delete_register()

# 利用者を削除した際に予約を削除する
def delete_user_and_register_and_reserve_without_conference():
    add_user('豊橋太郎', 'tarou@example.com')
    add_register()
    add_conference()
    add_reserve()
    delete_user()

# 全ての単体テストを実行
def all_unit_test():
    print("[test]:ユーザーテーブル単体テスト--------------------------------")
    test_User()
    print("[test]:登録者テーブル単体テスト----------------------------------")
    test_Register()
    print("[test]:会議室テーブル単体テスト----------------------------------")
    test_Conference()
    print("[test]:予約テーブル単体テスト------------------------------------")
    test_Reserve()
    print("[test]:備品テーブル単体テスト------------------------------------")
    test_Equipment()

