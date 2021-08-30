import typing
import db
from backend.models.course_model import Course


class CourseRepository:

    def __init__(self):
        pass

    def add(self, entity) -> int:
        db.CourseSQL.persist(entity)
        return 1

    def getAll(self) -> typing.List[Course]:
        course_list = db.CourseSQL.find()
        return course_list

    def getById(self, id: int) -> Course:
        course = db.CourseSQL.get(id=id)
        return course

    def getByCode(self, course_code: str) -> Course:
        course = db.CourseSQL.get(course_code=course_code)
        return course

    def findByTeacherId(self, teacher_id: int) -> typing.List[Course]:
        course_list = db.CourseSQL.find(teacher_id=teacher_id)
        return course_list
