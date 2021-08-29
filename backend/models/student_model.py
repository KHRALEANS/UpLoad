from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import relationship
from backend.models import Base


class Student(Base):
    __tablename__: str = 'student'

    id = Column(Integer, primary_key=True)
    student_name = Column(String(150))
    student_number = Column(Integer, unique=True)

    def __repr__(self):
        return f"<Student(id={self.id}, student_name={self.student_name}, student_number={self.student_number})>"

    def to_json(self):
        return {
            'id': self.id,
            'student_name': self.student_name,
            'student_number': self.student_number,
        }
