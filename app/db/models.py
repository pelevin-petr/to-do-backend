from sqlalchemy import (
    Column, Integer, String, MetaData, TIMESTAMP, ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base(metadata=MetaData())


class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    status = Column(String, nullable=False)
    description = Column(String)
    created_at = Column(TIMESTAMP, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("Users", back_populates="tasks")

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)

    tasks = relationship("Tasks", back_populates="user")
