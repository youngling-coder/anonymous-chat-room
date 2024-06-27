from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .base import Base
from .mixins import UserRelationMixin


class Message(UserRelationMixin, Base):

    _user_back_populates = "messages"

    content: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (id={self.id}, content={self.content}, owner_id={self.owner.id})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (id={self.id}, contente={self.content}, owner_id={self.owner.id})"
