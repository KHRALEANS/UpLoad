import inject
import db

from backend.repositorys.student_repository import StudentRepository

from backend.services.student_service import StudentService


def config_ioc(binder):
    student_repository = StudentRepository()

    student_service = StudentService()

    student_bind = db.StudentSQL

    binder.bind(StudentRepository, student_repository)

    binder.bind(StudentService, student_service)

    binder.bind(db.StudentSQL, student_bind)


inject.configure(config_ioc)

from flask import Flask
from flask_cors import CORS
from config import Config

from flask import Blueprint
from backend.uploadweb import bp as upload_module
from backend.api import bp as api_module


def create_app():
    db.init_db()
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'thisisthesecretkey'

    app.register_blueprint(upload_module, url_prefix='/blog')
    app.register_blueprint(api_module, url_prefix='/api')
    static_module = Blueprint('static_file', __name__, static_folder="public", static_url_path="/")
    app.register_blueprint(static_module, url_prefix='/')

    return app
