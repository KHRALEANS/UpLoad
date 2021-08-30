import inject
from flask import request, jsonify
from backend.models.student_model import Student
from backend.services.student_service import StudentService
from backend.api import bp

student_service = inject.instance(StudentService)

@bp.route('/students', methods=['POST'])
def create_student():
    student_name = request.json['student_name']
    student_number = request.json['student_number']

    student = Student(student_name=student_name, student_number=student_number)
    student_service.add(student)

    return jsonify(student.to_json())


@bp.route('/students', methods=['GET'])
def list_students():
    student_list = student_service.getAll()

    result = {
        'students': [item.to_json() for item in student_list]
    }

    return jsonify(result)


@bp.route('/students/<id>', methods=['GET'])
def get_student_by_id(id):
    student = student_service.getById(id)

    result = student.to_json()
    return jsonify(result)
