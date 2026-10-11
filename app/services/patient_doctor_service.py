from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.patient_doctor_repository import PatientDoctorRepository
from app.repositories.patient_repository import PatientRepository
from app.repositories.doctor_repositories import DoctorRepository


class PatientDoctorService:

    @staticmethod
    def assign_doctor(
        db: Session,
        patient_id: int,
        doctor_id: int
    ):
        patient = PatientRepository.get_by_id(db, patient_id)

        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )

        doctor = DoctorRepository.get_by_id(db, doctor_id)

        if not doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )

        existing_assignment = PatientDoctorRepository.get_assignment(
            db,
            patient_id,
            doctor_id
        )

        if existing_assignment:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Doctor is already assigned to this patient"
            )

        return PatientDoctorRepository.create(
            db,
            patient_id,
            doctor_id
        )

    @staticmethod
    def get_patient_doctors(
        db: Session,
        patient_id: int
    ):
        patient = PatientRepository.get_by_id(db, patient_id)

        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )

        return PatientDoctorRepository.get_by_patient(
            db,
            patient_id
        )

    @staticmethod
    def get_doctor_patients(
        db: Session,
        doctor_id: int
    ):
        doctor = DoctorRepository.get_by_id(db, doctor_id)

        if not doctor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Doctor not found"
            )

        return PatientDoctorRepository.get_by_doctor(
            db,
            doctor_id
        )

    @staticmethod
    def update_status(
        db: Session,
        patient_id: int,
        doctor_id: int,
        new_status: str
    ):
        assignment = PatientDoctorRepository.get_assignment(
            db,
            patient_id,
            doctor_id
        )

        if not assignment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient-doctor assignment not found"
            )

        allowed_statuses = {"active", "inactive"}

        if new_status not in allowed_statuses:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid assignment status"
            )

        return PatientDoctorRepository.update_status(
            db,
            assignment,
            new_status
        )

    @staticmethod
    def remove_assignment(
        db: Session,
        patient_id: int,
        doctor_id: int
    ):
        assignment = PatientDoctorRepository.get_assignment(
            db,
            patient_id,
            doctor_id
        )

        if not assignment:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient-doctor assignment not found"
            )

        PatientDoctorRepository.delete(
            db,
            assignment
        )