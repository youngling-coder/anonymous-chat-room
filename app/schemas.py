from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BaseUser(BaseModel):
    username: str


class CreateUser(BaseUser):
    password: str


class UserResponse(BaseUser):
    id: int
    model_config = ConfigDict(from_attributes=True)


class Message(BaseModel):
    content: str


class CreateMessage(Message):
    pass


class MessageResponse(Message):
    id: int
    owner: UserResponse

    model_config = ConfigDict(from_attributes=True)
