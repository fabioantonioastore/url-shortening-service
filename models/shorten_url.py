from uuid import uuid4
from datetime import datetime

from sqlalchemy import String, DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class ShortenURL(Base):
    __tablename__ = "shorten_urls"

    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid4())
    )
    url: Mapped[str] = mapped_column(String)
    short_code: Mapped[str] = mapped_column(String, unique=True)
    total_access: Mapped[int] = mapped_column(Integer, default=0)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    update_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
