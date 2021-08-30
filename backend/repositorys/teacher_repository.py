import typing
import db
from backend.models.teacher_model import Teacher


class TeacherRepository:

    def __init__(self):
        pass

    def add(self, entity) -> int:
        db.TeacherSQL.persist(entity)
        return 1

    def getAll(self) -> typing.List[Teacher]:
        teacher_list = db.TeacherSQL.find()
        return teacher_list

    def getById(self, id: int) -> Teacher:
        teacher = db.TeacherSQL.get(id=id)
        return teacher
