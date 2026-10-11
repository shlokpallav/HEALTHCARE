from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.family_history_repository import (
    FamilyHistoryRepository,
)
from app.schemas.family_history import (
    FamilyHistoryCreate,
    FamilyHistoryUpdate,
)


class FamilyHistoryService:

    @staticmethod
    def create_history(
        db: Session,
        history_data: FamilyHistoryCreate,
    ):
        return FamilyHistoryRepository.create(
            db,
            history_data,
        )

    @staticmethod
    def get_history(
        db: Session,
        family_history_id: int,
    ):
        history = FamilyHistoryRepository.get_by_id(
            db,
            family_history_id,
        )

        if not history:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Family medical history not found",
            )

        return history

    @staticmethod
    def get_patient_history(
        db: Session,
        patient_id: int,
    ):
        return FamilyHistoryRepository.get_by_patient(
            db,
            patient_id,
        )

    @staticmethod
    def update_history(
        db: Session,
        family_history_id: int,
        history_data: FamilyHistoryUpdate,
    ):
        history = FamilyHistoryRepository.get_by_id(
            db,
            family_history_id,
        )

        if not history:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Family medical history not found",
            )

        return FamilyHistoryRepository.update(
            db,
            history,
            history_data,
        )

    @staticmethod
    def delete_history(
        db: Session,
        family_history_id: int,
    ):
        history = FamilyHistoryRepository.get_by_id(
            db,
            family_history_id,
        )

        if not history:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Family medical history not found",
            )

        FamilyHistoryRepository.delete(
            db,
            history,
        )