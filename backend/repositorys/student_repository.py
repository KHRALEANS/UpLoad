import typing
import db
from backend.models.student_model import Student


class StudentRepository:

    def __init__(self):
        pass

    def add(self, entity) -> int:
        db.StudentSQL.persist(entity)
        return 1

    def getAll(self) -> typing.List[Student]:
        student_list = db.StudentSQL.find()
        return student_list

    def getById(self, id: int) -> Student:
        student = db.StudentSQL.get(id=id)
        return student
