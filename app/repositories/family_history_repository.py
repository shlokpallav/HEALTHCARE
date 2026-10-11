from sqlalchemy.orm import Session

from app.models.family_history import FamilyHistory
from app.schemas.family_history import (
    FamilyHistoryCreate,
    FamilyHistoryUpdate,
)


class FamilyHistoryRepository:

    @staticmethod
    def create(
        db: Session,
        history_data: FamilyHistoryCreate,
    ):
        history = FamilyHistory(
            **history_data.model_dump()
        )

        db.add(history)
        db.commit()
        db.refresh(history)

        return history

    @staticmethod
    def get_by_id(
        db: Session,
        family_history_id: int,
    ):
        return (
            db.query(FamilyHistory)
            .filter(
                FamilyHistory.family_history_id
                == family_history_id
            )
            .first()
        )

    @staticmethod
    def get_by_patient(
        db: Session,
        patient_id: int,
    ):
        return (
            db.query(FamilyHistory)
            .filter(
                FamilyHistory.patient_id == patient_id
            )
            .order_by(
                FamilyHistory.relation.asc()
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        history: FamilyHistory,
        history_data: FamilyHistoryUpdate,
    ):
        update_data = history_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(history, field, value)

        db.commit()
        db.refresh(history)

        return history

    @staticmethod
    def delete(
        db: Session,
        history: FamilyHistory,
    ):
        db.delete(history)
        db.commit()