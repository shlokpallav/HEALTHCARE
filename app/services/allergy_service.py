from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.allergy_repository import AllergyRepository
from app.schemas.allergy import AllergyCreate, AllergyUpdate


class AllergyService:

    @staticmethod
    def create_allergy(
        db: Session,
        allergy_data: AllergyCreate
    ):
        return AllergyRepository.create(
            db,
            allergy_data
        )

    @staticmethod
    def get_allergy(
        db: Session,
        allergy_id: int
    ):
        allergy = AllergyRepository.get_by_id(
            db,
            allergy_id
        )

        if not allergy:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Allergy not found"
            )

        return allergy

    @staticmethod
    def get_patient_allergies(
        db: Session,
        patient_id: int
    ):
        return AllergyRepository.get_by_patient(
            db,
            patient_id
        )

    @staticmethod
    def update_allergy(
        db: Session,
        allergy_id: int,
        allergy_data: AllergyUpdate
    ):
        allergy = AllergyRepository.get_by_id(
            db,
            allergy_id
        )

        if not allergy:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Allergy not found"
            )

        return AllergyRepository.update(
            db,
            allergy,
            allergy_data
        )

    @staticmethod
    def delete_allergy(
        db: Session,
        allergy_id: int
    ):
        allergy = AllergyRepository.get_by_id(
            db,
            allergy_id
        )

        if not allergy:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Allergy not found"
            )

        AllergyRepository.delete(
            db,
            allergy
        )