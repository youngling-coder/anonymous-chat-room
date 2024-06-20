from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, func
from .base import Base
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .message import Message


class User(Base):

    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    messages: Mapped[list["Message"]] = relationship("Message", back_populates="owner")
    password: Mapped[str] = mapped_column(String, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        server_default=func.now(), default=datetime.now
    )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} (id={self.id}, username={self.username})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} (id={self.id}, username={self.username})"
