from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.core.database import Base


class FamilyHistory(Base):
    __tablename__ = "family_medical_history"

    family_history_id = Column(
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

    relation = Column(
        String(100),
        nullable=False,
    )

    condition_name = Column(
        String(255),
        nullable=False,
    )

    diagnosed_age = Column(
        Integer,
        nullable=True,
    )

    status = Column(
        String(20),
        nullable=False,
        default="confirmed",
    )

    notes = Column(
        String(500),
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