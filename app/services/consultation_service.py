from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.consultation_repository import (
    ConsultationRepository,
)
from app.repositories.patient_repository import PatientRepository
from app.repositories.doctor_repositories import DoctorRepository
from app.schemas.consultation import (
    ConsultationCreate,
    ConsultationUpdate,
)


class ConsultationService:

    @staticmethod
    def create_consultation(
        db: Session,
        consultation_data: ConsultationCreate,
    ):
        patient = PatientRepository.get_by_id(
            db,
            consultation_data.patient_id,
        )

        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found",
            )

        doctor = DoctorRepository.get_by_id(
            db,
            consultation_data.doctor_id,
        )

        if not doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found",
            )

        return ConsultationRepository.create(
            db,
            consultation_data,
        )

    @staticmethod
    def get_consultation(
        db: Session,
        consultation_id: int,
    ):
        consultation = ConsultationRepository.get_by_id(
            db,
            consultation_id,
        )

        if not consultation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Consultation not found",
            )

        return consultation

    @staticmethod
    def get_patient_consultations(
        db: Session,
        patient_id: int,
    ):
        patient = PatientRepository.get_by_id(
            db,
            patient_id,
        )

        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found",
            )

        return ConsultationRepository.get_by_patient(
            db,
            patient_id,
        )

    @staticmethod
    def get_doctor_consultations(
        db: Session,
        doctor_id: int,
    ):
        doctor = DoctorRepository.get_by_id(
            db,
            doctor_id,
        )

        if not doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found",
            )

        return ConsultationRepository.get_by_doctor(
            db,
            doctor_id,
        )

    @staticmethod
    def update_consultation(
        db: Session,
        consultation_id: int,
        consultation_data: ConsultationUpdate,
    ):
        consultation = ConsultationRepository.get_by_id(
            db,
            consultation_id,
        )

        if not consultation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Consultation not found",
            )

        return ConsultationRepository.update(
            db,
            consultation,
            consultation_data,
        )

    @staticmethod
    def delete_consultation(
        db: Session,
        consultation_id: int,
    ):
        consultation = ConsultationRepository.get_by_id(
            db,
            consultation_id,
        )

        if not consultation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Consultation not found",
            )

        ConsultationRepository.delete(
            db,
            consultation,
        )