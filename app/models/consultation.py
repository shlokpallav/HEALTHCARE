from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base


class Consultation(Base):
    __tablename__ = "consultations"

    consultation_id = Column(
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

    doctor_id = Column(
        Integer,
        ForeignKey("doctors.doctor_id"),
        nullable=False,
    )

    consultation_date = Column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )

    symptoms = Column(
        Text,
        nullable=True,
    )

    diagnosis = Column(
        Text,
        nullable=True,
    )

    notes = Column(
        Text,
        nullable=True,
    )

    prescription = Column(
        Text,
        nullable=True,
    )

    follow_up_date = Column(
        DateTime,
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