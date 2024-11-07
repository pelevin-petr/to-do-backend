from datetime import datetime

from pydantic import BaseModel, Field


class BaseTask(BaseModel):
    title: str = Field(min_length=1)
    status: str = Field(min_length=1)
    description: str = Field(min_length=0)


class CreateTask(BaseTask):
    pass


class Task(BaseTask):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
