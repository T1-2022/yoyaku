from flask import Blueprint, render_template

user_info_bp = Blueprint('user_info', __name__, url_prefix='/user_info')

@user_info_bp.route('/')
def user_information():
    return render_template('user_info.html')