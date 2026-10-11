from sqlalchemy.orm import Session

from app.models.medication import Medication
from app.schemas.medication import MedicationCreate, MedicationUpdate


class MedicationRepository:

    @staticmethod
    def create(
        db: Session,
        medication_data: MedicationCreate,
    ):
        medication = Medication(
            **medication_data.model_dump()
        )

        db.add(medication)
        db.commit()
        db.refresh(medication)

        return medication

    @staticmethod
    def get_by_id(
        db: Session,
        medication_id: int,
    ):
        return (
            db.query(Medication)
            .filter(
                Medication.medication_id == medication_id
            )
            .first()
        )

    @staticmethod
    def get_by_patient(
        db: Session,
        patient_id: int,
    ):
        return (
            db.query(Medication)
            .filter(
                Medication.patient_id == patient_id
            )
            .order_by(
                Medication.start_date.desc()
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        medication: Medication,
        medication_data: MedicationUpdate,
    ):
        update_data = medication_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(medication, field, value)

        db.commit()
        db.refresh(medication)

        return medication

    @staticmethod
    def delete(
        db: Session,
        medication: Medication,
    ):
        db.delete(medication)
        db.commit()