import inject
from flask import request, jsonify
from backend.models.course_model import Course
from backend.services.course_service import CourseService
from backend.models.homework_model import Homework
from backend.services.homework_service import HomeworkService
from backend.api import bp

course_service = inject.instance(CourseService)
homework_service = inject.instance(HomeworkService)

@bp.route('/courses/<courseCode>/homeworks', methods=['POST'])
def create_course_homework(courseCode):
    course = course_service.getByCode(courseCode)
    teacher_id = course.teacher_id
    student_id = course.student_id
    course_id = course.id
    assignment = request.json['assignment']

    homework = Homework(teacher_id=teacher_id, student_id=student_id, course_id=course_id, assignment=assignment)
    homework_service.add(homework)

    return jsonify(homework.to_json())


@bp.route('/courses/<courseCode>/homeworks', methods=['GET'])
def find_course_homework(courseCode):
    course = course_service.getByCode(courseCode)
    course_id = course.id
    homeworks = homework_service.findByCourseId(course_id)

    result = {
        'homeworks': [item.to_json() for item in homeworks]
    }

    return jsonify(result)


@bp.route('/courses/<courseCode>/homeworks/<id>', methods=['GET'])
def get_course_homework_by_id(courseCode, id):
    course = course_service.getByCode(courseCode)
    homework = homework_service.getById(id)

    result = {
        'course': course.to_json(),
        'homework': homework.to_json()
    }

    return jsonify(result)
