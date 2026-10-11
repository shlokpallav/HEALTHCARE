from sqlalchemy.orm import Session

from app.models.consultation import Consultation
from app.schemas.consultation import (
    ConsultationCreate,
    ConsultationUpdate,
)


class ConsultationRepository:

    @staticmethod
    def create(
        db: Session,
        consultation_data: ConsultationCreate,
    ):
        consultation = Consultation(
            **consultation_data.model_dump(
                exclude_none=True
            )
        )

        db.add(consultation)
        db.commit()
        db.refresh(consultation)

        return consultation

    @staticmethod
    def get_by_id(
        db: Session,
        consultation_id: int,
    ):
        return (
            db.query(Consultation)
            .filter(
                Consultation.consultation_id == consultation_id
            )
            .first()
        )

    @staticmethod
    def get_by_patient(
        db: Session,
        patient_id: int,
    ):
        return (
            db.query(Consultation)
            .filter(
                Consultation.patient_id == patient_id
            )
            .order_by(
                Consultation.consultation_date.desc()
            )
            .all()
        )

    @staticmethod
    def get_by_doctor(
        db: Session,
        doctor_id: int,
    ):
        return (
            db.query(Consultation)
            .filter(
                Consultation.doctor_id == doctor_id
            )
            .order_by(
                Consultation.consultation_date.desc()
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        consultation: Consultation,
        consultation_data: ConsultationUpdate,
    ):
        update_data = consultation_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(consultation, field, value)

        db.commit()
        db.refresh(consultation)

        return consultation

    @staticmethod
    def delete(
        db: Session,
        consultation: Consultation,
    ):
        db.delete(consultation)
        db.commit()