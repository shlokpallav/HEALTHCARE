from sqlalchemy.orm import Session

from app.models.allergy import Allergy
from app.schemas.allergy import AllergyCreate, AllergyUpdate


class AllergyRepository:

    @staticmethod
    def create(
        db: Session,
        allergy_data: AllergyCreate
    ) -> Allergy:

        allergy = Allergy(
            patient_id=allergy_data.patient_id,
            allergy_name=allergy_data.allergy_name,
            allergy_type=allergy_data.allergy_type,
            reaction=allergy_data.reaction,
            severity=allergy_data.severity,
            diagnosed_date=allergy_data.diagnosed_date,
            source_report_id=allergy_data.source_report_id,
        )

        db.add(allergy)
        db.commit()
        db.refresh(allergy)

        return allergy

    @staticmethod
    def get_by_id(
        db: Session,
        allergy_id: int
    ) -> Allergy | None:

        return db.get(Allergy, allergy_id)

    @staticmethod
    def get_by_patient(
        db: Session,
        patient_id: int
    ) -> list[Allergy]:

        return (
            db.query(Allergy)
            .filter(Allergy.patient_id == patient_id)
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        allergy: Allergy,
        allergy_data: AllergyUpdate
    ) -> Allergy:

        update_data = allergy_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(allergy, field, value)

        db.commit()
        db.refresh(allergy)

        return allergy

    @staticmethod
    def delete(
        db: Session,
        allergy: Allergy
    ) -> None:

        db.delete(allergy)
        db.commit()
        