from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional


class User(BaseModel):
    username: str


class CreateUser(User):
    password: str


class UserResponse(User):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)


class Message(BaseModel):
    content: str


class CreateMessage(Message):
    pass


class MessageResponse(Message):
    id: int
    owner: UserResponse

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


class TokenData(BaseModel):
    id: Optional[str]
