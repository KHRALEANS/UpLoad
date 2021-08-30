from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import relationship
from backend.models import Base


class Homework(Base):
    __tablename__: str = 'homeworks'

    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    student_id = Column(Integer, ForeignKey('student.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    assignment = Column(String(150))

    teacher = relationship("Teacher", back_populates="homeworks")
    student = relationship("Student", back_populates="homeworks")
    course = relationship("Course", back_populates="homeworks")

    def __repr__(self):
        return f"<Teacher(id={self.id}, teacher_name={self.teacher_name}, teacher_email={self.teacher_email}, teacher_password={self.teacher_password})>"

    def to_json(self):
        return {
            'id': self.id,
            'teacher_name': self.teacher_name,
            'teacher_email': self.teacher_email,
            'teacher_password': self.teacher_password
        }
