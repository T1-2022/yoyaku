'''
    created at 2022/02/03
    created by shinoda hiroki

    @this file is ...
    
    routing site to change user's informarion
'''
from flask import Blueprint, render_template, session, redirect, url_for
from login import login_required

# ブル-プリントをインスタンス化
user_info_bp = Blueprint('user_info', __name__, url_prefix='/user_info')

# ユーザーネーム変更ページを表示
@user_info_bp.route('/change_name', methods=['GET'])
def change_user_name():
    if login_required():
        return render_template('change_user_info/change_user_name.html')
    # 認証失敗したら、ログインページへ
    return redirect(url_for('login.login'))

# ユーザーパスワード変更ページを表示
@user_info_bp.route('/change_passwd', methods=['GET'])
def change_user_passwd():
    if login_required():
        return render_template('change_user_info/change_user_passwd.html')
    # 認証失敗したら、ログインページへ
    return redirect(url_for('login.login'))

# ユーザーメールアドレス変更ページを表示
@user_info_bp.route('/change_mail', methods=['GET'])
def change_user_mail():
    if login_required():
        return render_template('change_user_info/change_user_mail.html')
    # 認証失敗したら、ログインページへ
    return redirect(url_for('login.login'))

@user_info_bp.route('/logout', methods=["GET"])
def logout():
    if login_required():
        # セッション情報を削除
        session.pop('user', None)
        session.pop('flag', None)
    return redirect(url_for('login.login'))