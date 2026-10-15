"""Modelos relacionais que serão completados na atividade 2."""

import datetime

from sqlalchemy import CheckConstraint, Date, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Event(Base):
    __tablename__ = "events"
    # A regra fica no banco: nem um INSERT direto aceita capacidade <= 0.
    __table_args__ = (CheckConstraint("capacity > 0", name="ck_events_capacity_positive"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    # `datetime.date` em vez de `date`: o atributo também se chama `date`.
    date: Mapped[datetime.date] = mapped_column(Date)
    capacity: Mapped[int] = mapped_column(Integer)


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    # Dois usuários não podem compartilhar o mesmo e-mail.
    email: Mapped[str] = mapped_column(String, unique=True)


class Registration(Base):
    __tablename__ = "registrations"
    # O mesmo usuário não pode se inscrever duas vezes no mesmo evento.
    __table_args__ = (UniqueConstraint("event_id", "user_id", name="uq_registrations_event_user"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey("events.id"))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
