from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, func
from .base import Base
from .mixins import UserRelationMixin


class Message(UserRelationMixin, Base):

    _user_back_populates = "messages"

    content: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (id={self.id}, content={self.content}, owner_id={self.owner.id})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (id={self.id}, contente={self.content}, owner_id={self.owner.id})"
