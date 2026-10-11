from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class PatientDoctor(Base):
    __tablename__ = "patient_doctors"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.patient_id"),
        nullable=False
    )

    doctor_id: Mapped[int] = mapped_column(
        ForeignKey("doctors.doctor_id"),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="active"
    )

    assigned_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )