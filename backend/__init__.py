import inject
import db

from backend.repositorys.student_repository import StudentRepository
from backend.repositorys.teacher_repository import TeacherRepository
from backend.repositorys.course_repository import CourseRepository
from backend.repositorys.homework_repository import HomeworkRepository

from backend.services.student_service import StudentService
from backend.services.teacher_service import TeacherService
from backend.services.course_service import CourseService
from backend.services.homework_service import HomeworkService


def config_ioc(binder):
    student_repository = StudentRepository()
    teacher_repository = TeacherRepository()
    course_repository = CourseRepository()
    homework_repository = HomeworkRepository()

    student_service = StudentService()
    teacher_service = TeacherService()
    course_service = CourseService()
    homework_service = HomeworkService()

    student_bind = db.StudentSQL
    teacher_bind = db.TeacherSQL
    course_bind = db.CourseSQL
    homework_bind = db.HomeworkSQL

    binder.bind(StudentRepository, student_repository)
    binder.bind(TeacherRepository, teacher_repository)
    binder.bind(CourseRepository, course_repository)
    binder.bind(HomeworkRepository, homework_repository)

    binder.bind(StudentService, student_service)
    binder.bind(TeacherService, teacher_service)
    binder.bind(CourseService, course_service)
    binder.bind(HomeworkService, homework_service)

    binder.bind(db.StudentSQL, student_bind)
    binder.bind(db.TeacherSQL, teacher_bind)
    binder.bind(db.CourseSQL, course_bind)
    binder.bind(db.HomeworkSQL, homework_bind)


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
