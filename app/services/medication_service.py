from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.medication_repository import MedicationRepository
from app.schemas.medication import MedicationCreate, MedicationUpdate


class MedicationService:

    @staticmethod
    def create_medication(
        db: Session,
        medication_data: MedicationCreate,
    ):
        return MedicationRepository.create(
            db,
            medication_data,
        )

    @staticmethod
    def get_medication(
        db: Session,
        medication_id: int,
    ):
        medication = MedicationRepository.get_by_id(
            db,
            medication_id,
        )

        if not medication:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medication not found",
            )

        return medication

    @staticmethod
    def get_patient_medications(
        db: Session,
        patient_id: int,
    ):
        return MedicationRepository.get_by_patient(
            db,
            patient_id,
        )

    @staticmethod
    def update_medication(
        db: Session,
        medication_id: int,
        medication_data: MedicationUpdate,
    ):
        medication = MedicationRepository.get_by_id(
            db,
            medication_id,
        )

        if not medication:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medication not found",
            )

        return MedicationRepository.update(
            db,
            medication,
            medication_data,
        )

    @staticmethod
    def delete_medication(
        db: Session,
        medication_id: int,
    ):
        medication = MedicationRepository.get_by_id(
            db,
            medication_id,
        )

        if not medication:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medication not found",
            )

        MedicationRepository.delete(
            db,
            medication,
        )