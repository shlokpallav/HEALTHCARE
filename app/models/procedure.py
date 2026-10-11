from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base


class Procedure(Base):
    __tablename__ = "procedures"

    procedure_id = Column(
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

    procedure_name = Column(
        String(255),
        nullable=False,
    )

    procedure_date = Column(
        Date,
        nullable=True,
    )

    reason = Column(
        String(500),
        nullable=True,
    )

    hospital = Column(
        String(255),
        nullable=True,
    )

    surgeon_or_doctor = Column(
        String(255),
        nullable=True,
    )

    outcome = Column(
        String(500),
        nullable=True,
    )

    status = Column(
        String(50),
        nullable=False,
        default="pending",
    )

    source_report_id = Column(
        Integer,
        ForeignKey("medical_reports.report_id"),
        nullable=True,
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