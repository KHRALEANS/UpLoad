from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

from backend.models.student_model import Student
from backend.repositorys.base_repository import FSQLAlchemyRepository

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
DBSession = sessionmaker(bind=engine)
session = DBSession()

StudentSQL = FSQLAlchemyRepository(Student, session)

from backend.models import my_metadata


def init_db():
    my_metadata.create_all(bind=engine)
