from flask import Blueprint

bp = Blueprint('api', __name__)

from backend.api import student_api, teacher_api, course_api, homework_api
