from flask import Flask
from flask import render_template, login_required, current_user, logout_user


main_view = Flask(__name__)
@main_view.route("/", methods=["GET"]) ##予約情報
@login_required
def book_info():
    return render_template(".html", name=current_user.name)

@main_view.route("/", methods=["GET"]) ##予約する
def booking():
    return render_template(".html", name=current_user.name)

@main_view.route("/", methods=["GET"]) ##会議室詳細
def room():
    return render_template(".html", name=current_user.name)

@main_view.route("/", methods=["GET"]) ##オンラインヘルプ
def help():
    return render_template(".html", name=current_user.name)

@main_view.route("/", methods=["GET"]) ##ユーザー情報
def user_info():
    return render_template(".html", name=current_user.name)

@main_view.route('/')   ##ログアウト
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))



if __name__ == '__main__':
    main_view.run(debug=True)
