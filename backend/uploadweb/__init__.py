from flask import Blueprint

bp = Blueprint('upload_app', __name__, template_folder="../../frontend/dist/",
               static_folder="../../frontend/dist/upload/lib", url_prefix='/upload')
