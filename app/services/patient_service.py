from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.patient_repository import PatientRepository
from app.schemas.patient import PatientCreate


class PatientService:

    @staticmethod
    def create_patient(
        db: Session,
        patient_data: PatientCreate
    ):
        return PatientRepository.create(
            db,
            patient_data
        )

    @staticmethod
    def get_patient(
        db: Session,
        patient_id: int
    ):
        patient = PatientRepository.get_by_id(
            db,
            patient_id
        )

        if patient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )

        return patient
    
    @staticmethod
    def update_patient(
        db: Session,
        patient_id: int,
        patient_data: PatientUpdate
    ):
        patient = PatientRepository.get_by_id(
            db,
            patient_id
        )

        if patient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )

        return PatientRepository.update(
            db,
            patient,
            patient_data
        )
    @staticmethod
    def delete_patient(
        db: Session,
        patient_id: int
    ):
        patient = PatientRepository.get_by_id(
            db,
            patient_id
        )

        if patient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )

        PatientRepository.delete(
            db,
            patient
        )

        return {
            "message": "Patient deleted successfully"
        }