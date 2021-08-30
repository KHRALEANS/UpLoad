import typing
import db
from backend.models.homework_model import Homework


class HomeworkRepository:

    def __init__(self):
        pass

    def add(self, entity) -> int:
        db.HomeworkSQL.persist(entity)
        return 1

    def getAll(self) -> typing.List[Homework]:
        homework_list = db.HomeworkSQL.find()
        return homework_list

    def getById(self, id: int) -> Homework:
        homework = db.HomeworkSQL.get(id=id)
        return homework

    def findByCourseId(self, course_id: int) -> typing.List[Homework]:
        homework_list = db.HomeworkSQL.find(course_id=course_id)
        return homework_list
