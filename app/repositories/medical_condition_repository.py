from sqlalchemy.orm import Session

from app.models.medical_condition import MedicalCondition
from app.schemas.medical_condition import (
    MedicalConditionCreate,
    MedicalConditionUpdate,
)


class MedicalConditionRepository:

    @staticmethod
    def create(
        db: Session,
        condition_data: MedicalConditionCreate
    ) -> MedicalCondition:

        condition = MedicalCondition(
            patient_id=condition_data.patient_id,
            condition_name=condition_data.condition_name,
            diagnosed_date=condition_data.diagnosed_date,
            source_report_id=condition_data.source_report_id,
        )

        db.add(condition)
        db.commit()
        db.refresh(condition)

        return condition

    @staticmethod
    def get_by_id(
        db: Session,
        condition_id: int
    ) -> MedicalCondition | None:

        return db.get(MedicalCondition, condition_id)

    @staticmethod
    def get_by_patient_id(
        db: Session,
        patient_id: int
    ) -> list[MedicalCondition]:

        return (
            db.query(MedicalCondition)
            .filter(
                MedicalCondition.patient_id == patient_id
            )
            .order_by(
                MedicalCondition.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        condition: MedicalCondition,
        condition_data: MedicalConditionUpdate
    ) -> MedicalCondition:

        update_data = condition_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(condition, field, value)

        db.commit()
        db.refresh(condition)

        return condition

    @staticmethod
    def delete(
        db: Session,
        condition: MedicalCondition
    ) -> None:

        db.delete(condition)
        db.commit()