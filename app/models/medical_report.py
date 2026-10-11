from datetime import date, datetime

from sqlalchemy import String, Date, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class MedicalReport(Base):
    __tablename__ = "medical_reports"

    report_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.patient_id"),
        nullable=False
    )

    report_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    report_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    report_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    file_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default = datetime.utcnow,
        nullable=False
    )