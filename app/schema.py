from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    phone: str


class Group(BaseModel):
    name: str
    title: str
    description: str