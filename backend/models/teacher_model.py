from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy.orm import relationship
from backend.models import Base


class Teacher(Base):
    __tablename__: str = 'teacher'

    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(150))
    teacher_email = Column(String(150), unique=True)
    teacher_password = Column(String(150))

    homeworks = relationship("Homework", order_by='Homework.id', back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(id={self.id}, teacher_name={self.teacher_name}, teacher_email={self.teacher_email}, teacher_password={self.teacher_password})>"

    def to_json(self):
        return {
            'id': self.id,
            'teacher_name': self.teacher_name,
            'teacher_email': self.teacher_email,
            'teacher_password': self.teacher_password
        }
