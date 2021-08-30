import inject
from flask import request, jsonify
from backend.models.teacher_model import Teacher
from backend.services.teacher_service import TeacherService
from backend.models.course_model import Course
from backend.services.course_service import CourseService
from backend.api import bp

teacher_service = inject.instance(TeacherService)
course_service = inject.instance(CourseService)

@bp.route('/teachers', methods=['POST'])
def create_teacher():
    teacher_name = request.json['teacher_name']
    teacher_email = request.json['teacher_email']
    teacher_password = request.json['teacher_password']

    teacher = Teacher(teacher_name=teacher_name, teacher_email=teacher_email, teacher_password=teacher_password)
    teacher_service.add(teacher)

    return jsonify(teacher.to_json())


@bp.route('/students', methods=['GET'])
def list_teachers():
    teacher_list = teacher_service.getAll()

    result = {
        'teachers': [item.to_json() for item in teacher_list]
    }

    return jsonify(result)


@bp.route('/teachers/<id>', methods=['GET'])
def get_teacher_by_id(id):
    teacher = teacher_service.getById(id)

    result = teacher.to_json()
    return jsonify(result)


@bp.route('/teachers/<id>/courses', methods=['POST'])
def teacher_create_course(id):
    course_code = request.json['course_code']
    teacher_id = id

    course = Course(course_code=course_code, teacher_id=teacher_id)
    course_service.add(course)

    return jsonify(course.to_json())


@bp.route('/teachers/<id>/courses', methods=['GET'])
def find_teacher_courses(id):
    courses = course_service.findByTeacherId(id)

    result = {
        'courses': [item.to_json() for item in courses]
    }

    return jsonify(result)


@bp.route('/teachers/<id>/courses/<courseCode>', methods=['GET'])
def find_teacher_courses(id, courseCode):
    teacher = teacher_service.getById(id)
    course = course_service.getByCode(courseCode)

    result = {
        'teacher': teacher.to_json(),
        'course': course.to_json()
    }

    return jsonify(result)


@bp.route('/teachers/<id>/courses/<courseCode>', methods=['POST'])
def teacher_add_student_to_course(id, courseCode):
    teacher_id = id
    course_code = courseCode
    student_id = request.json['student_id']

    course = Course(course_code=course_code, teacher_id=teacher_id, student_id=student_id)
    course_service.add(course)

    return jsonify(course.to_json())
