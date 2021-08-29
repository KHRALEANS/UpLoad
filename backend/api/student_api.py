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
