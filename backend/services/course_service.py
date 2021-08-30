import inject
import typing
from backend.models.course_model import Course
from backend.repositorys.course_repository import CourseRepository


class CourseService:

    course_repository = inject.attr(CourseRepository)

    def add(self, entity) -> int:
        self.course_repository.add(entity)
        return 1

    def getById(self, id: int) -> Course:
        course = self.course_repository.getById(id)
        return course

    def getAll(self) -> typing.List[Course]:
        course_list = self.course_repository.getAll()
        return course_list

    def getByCode(self, course_code: str) -> Course:
        course = self.course_repository.getByCode(course_code)
        return course

    def findByTeacherId(self, teacher_id: int) -> typing.List[Course]:
        course_list = self.course_repository.findByTeacherId(teacher_id)
        return course_list
