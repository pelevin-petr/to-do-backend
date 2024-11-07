from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserAuth(BaseModel):
    username: str
    password: str

