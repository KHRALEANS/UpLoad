import inject
import typing
from backend.models.student_model import Student
from backend.repositorys.student_repository import StudentRepository


class StudentService:

    student_repository = inject.attr(StudentRepository)

    def add(self, entity) -> int:
        self.student_repository.add(entity)
        return 1

    def getById(self, id: int) -> Student:
        student = self.student_repository.getById(id)
        return student

    def getAll(self) -> typing.List[Student]:
        student_list = self.student_repository.getAll()
        return student_list
