from datetime import date

from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, ForeignKey
from app.core.database import Base


class Patient(Base):
    __tablename__ = "patients"

    patient_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    
    user_id: Mapped[int] = mapped_column(
    ForeignKey("users.user_id"),
    nullable=False,
    unique=True
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    date_of_birth: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    gender: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    address: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )