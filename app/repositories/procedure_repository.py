from sqlalchemy.orm import Session

from app.models.procedure import Procedure
from app.schemas.procedure import ProcedureCreate, ProcedureUpdate


class ProcedureRepository:

    @staticmethod
    def create(
        db: Session,
        procedure_data: ProcedureCreate,
    ):
        procedure = Procedure(
            **procedure_data.model_dump()
        )

        db.add(procedure)
        db.commit()
        db.refresh(procedure)

        return procedure

    @staticmethod
    def get_by_id(
        db: Session,
        procedure_id: int,
    ):
        return (
            db.query(Procedure)
            .filter(
                Procedure.procedure_id == procedure_id
            )
            .first()
        )

    @staticmethod
    def get_by_patient(
        db: Session,
        patient_id: int,
    ):
        return (
            db.query(Procedure)
            .filter(
                Procedure.patient_id == patient_id
            )
            .order_by(
                Procedure.procedure_date.desc()
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        procedure: Procedure,
        procedure_data: ProcedureUpdate,
    ):
        update_data = procedure_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(procedure, field, value)

        db.commit()
        db.refresh(procedure)

        return procedure

    @staticmethod
    def delete(
        db: Session,
        procedure: Procedure,
    ):
        db.delete(procedure)
        db.commit()