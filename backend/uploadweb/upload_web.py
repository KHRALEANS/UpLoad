from flask import render_template
from backend.uploadweb import bp


@bp.route('/', defaults={'path': ''})
@bp.route('/<path:u_path>')
def catch_all(u_path):
    return render_template('index.html')
