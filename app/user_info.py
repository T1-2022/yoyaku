'''
    created at 2022/02/03
    created by shinoda hiroki

    @this file is ...
    
    routing site to change user's informarion
'''

from flask import Blueprint, render_template, session, redirect, url_for

# ブル-プリントをインスタンス化
user_info_bp = Blueprint('user_info', __name__, url_prefix='/user_info')

# ユーザーネーム変更ページを表示
@user_info_bp.route('/change_name', methods=['GET'])
def change_user_name():
    return render_template('change_user_info/change_user_name.html')

# ユーザーパスワード変更ページを表示
@user_info_bp.route('/change_passwd', methods=['GET'])
def change_user_passwd():
    return render_template('change_user_info/change_user_passwd.html')

# ユーザーメールアドレス変更ページを表示
@user_info_bp.route('/change_mail', methods=['GET'])
def change_user_mail():
    return render_template('change_user_info/change_user_mail.html')

@user_info_bp.route('/logout', methods=["GET"])
def logout():
    session.pop('user', None)
    session.pop('flag', None)
    return redirect(url_for('login.login'))