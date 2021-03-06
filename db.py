from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

from backend.models.student_model import Student
from backend.models.teacher_model import Teacher
from backend.models.course_model import Course
from backend.models.homework_model import Homework
from backend.repositorys.base_repository import FSQLAlchemyRepository

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
DBSession = sessionmaker(bind=engine)
session = DBSession()

StudentSQL = FSQLAlchemyRepository(Student, session)
TeacherSQL = FSQLAlchemyRepository(Teacher, session)
CourseSQL = FSQLAlchemyRepository(Course, session)
HomeworkSQL = FSQLAlchemyRepository(Homework, session)

from backend.models import my_metadata


def init_db():
    my_metadata.create_all(bind=engine)
