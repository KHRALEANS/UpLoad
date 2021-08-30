from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import relationship
from backend.models import Base


class Course(Base):
    __tablename__: str = 'course'

    id = Column(Integer, primary_key=True)
    course_code = Column(String(150))
    teacher_id = Column(Integer)
    student_id = Column(Integer)

    homeworks = relationship("Homework", order_by='Homework.id', back_populates="course")

    def __repr__(self):
        return f"<Course(id={self.id}, course_code={self.course_code}, teacher_id={self.teacher_id}, student_id={self.student_id})>"

    def to_json(self):
        return {
            'id': self.id,
            'course_code': self.course_code,
            'teacher_id': self.teacher_id,
            'student_id': self.student_id
        }
