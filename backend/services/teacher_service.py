import inject
import typing
from backend.models.teacher_model import Teacher
from backend.repositorys.teacher_repository import TeacherRepository


class TeacherService:

    teacher_repository = inject.attr(TeacherRepository)

    def add(self, entity) -> int:
        self.teacher_repository.add(entity)
        return 1

    def getById(self, id: int) -> Teacher:
        teacher = self.teacher_repository.getById(id)
        return teacher

    def getAll(self) -> typing.List[Teacher]:
        teacher_list = self.teacher_repository.getAll()
        return teacher_list
