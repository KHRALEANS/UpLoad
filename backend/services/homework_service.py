import inject
import typing
from backend.models.homework_model import Homework
from backend.repositorys.homework_repository import HomeworkRepository


class HomeworkService:

    homework_repository = inject.attr(HomeworkRepository)

    def add(self, entity) -> int:
        self.homework_repository.add(entity)
        return 1

    def getById(self, id: int) -> Homework:
        homework = self.homework_repository.getById(id)
        return homework

    def getAll(self) -> typing.List[Homework]:
        homework_list = self.homework_repository.getAll()
        return homework_list

    def findByCourseId(self, course_id: int) -> typing.List[Homework]:
        homework_list = self.homework_repository.findByCourseId(course_id)
        return homework_list
