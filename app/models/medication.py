from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base


class Medication(Base):
    __tablename__ = "medications"

    medication_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
    )

    patient_id = Column(
        Integer,
        ForeignKey("patients.patient_id"),
        nullable=False,
    )

    medicine_name = Column(
        String(255),
        nullable=False,
    )

    dosage = Column(
        String(100),
        nullable=True,
    )

    frequency = Column(
        String(100),
        nullable=True,
    )

    route = Column(
        String(50),
        nullable=True,
    )

    start_date = Column(
        Date,
        nullable=True,
    )

    end_date = Column(
        Date,
        nullable=True,
    )

    reason = Column(
        String(500),
        nullable=True,
    )

    prescribed_by = Column(
        String(255),
        nullable=True,
    )

    source_report_id = Column(
        Integer,
        ForeignKey("medical_reports.report_id"),
        nullable=True,
    )

    status = Column(
        String(20),
        nullable=False,
        default="pending",
    )

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )