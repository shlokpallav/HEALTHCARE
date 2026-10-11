from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.doctor_repositories import DoctorRepository
from app.schemas.doctor import DoctorCreate, DoctorUpdate


class DoctorService:

    @staticmethod
    def create_doctor(
        db: Session,
        doctor_data: DoctorCreate,
    ):
        return DoctorRepository.create(
            db,
            doctor_data,
        )

    @staticmethod
    def get_doctor(
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

        return doctor

    @staticmethod
    def get_all_doctors(
        db: Session,
    ):
        return DoctorRepository.get_all(db)

    @staticmethod
    def update_doctor(
        db: Session,
        doctor_id: int,
        doctor_data: DoctorUpdate,
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

        return DoctorRepository.update(
            db,
            doctor,
            doctor_data,
        )

    @staticmethod
    def delete_doctor(
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

        DoctorRepository.delete(
            db,
            doctor,
        )