from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.medical_condition import MedicalCondition
from app.repositories.medical_condition_repository import (
    MedicalConditionRepository,
)
from app.schemas.medical_condition import (
    MedicalConditionCreate,
    MedicalConditionUpdate,
)


class MedicalConditionService:

    @staticmethod
    def create_condition(
        db: Session,
        condition_data: MedicalConditionCreate
    ) -> MedicalCondition:

        return MedicalConditionRepository.create(
            db,
            condition_data
        )

    @staticmethod
    def get_condition(
        db: Session,
        condition_id: int
    ) -> MedicalCondition:

        condition = MedicalConditionRepository.get_by_id(
            db,
            condition_id
        )

        if not condition:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medical condition not found"
            )

        return condition

    @staticmethod
    def get_patient_conditions(
        db: Session,
        patient_id: int
    ) -> list[MedicalCondition]:

        return MedicalConditionRepository.get_by_patient_id(
            db,
            patient_id
        )

    @staticmethod
    def update_condition(
        db: Session,
        condition_id: int,
        condition_data: MedicalConditionUpdate
    ) -> MedicalCondition:

        condition = MedicalConditionRepository.get_by_id(
            db,
            condition_id
        )

        if not condition:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medical condition not found"
            )

        return MedicalConditionRepository.update(
            db,
            condition,
            condition_data
        )

    @staticmethod
    def delete_condition(
        db: Session,
        condition_id: int
    ) -> None:

        condition = MedicalConditionRepository.get_by_id(
            db,
            condition_id
        )

        if not condition:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medical condition not found"
            )

        MedicalConditionRepository.delete(
            db,
            condition
        )