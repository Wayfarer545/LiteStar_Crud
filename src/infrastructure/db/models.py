import datetime as dt

from sqlalchemy import BigInteger, String, TIMESTAMP
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column


def get_time() -> dt:
    return dt.datetime.now(dt.UTC)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[BigInteger] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(60), nullable=False)
    created_at: Mapped[dt.datetime] = mapped_column(TIMESTAMP, default_factory=get_time)
    updated_at: Mapped[dt.datetime] = mapped_column(TIMESTAMP, default_factory=get_time)

