from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class MedicalCondition(Base):
    __tablename__ = "medical_conditions"

    condition_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.patient_id"),
        nullable=False
    )

    condition_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    diagnosed_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    source_report_id: Mapped[int | None] = mapped_column(
        ForeignKey("medical_reports.report_id"),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="pending"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )