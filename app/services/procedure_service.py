from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.procedure_repository import ProcedureRepository
from app.schemas.procedure import ProcedureCreate, ProcedureUpdate


class ProcedureService:

    @staticmethod
    def create_procedure(
        db: Session,
        procedure_data: ProcedureCreate,
    ):
        return ProcedureRepository.create(
            db,
            procedure_data,
        )

    @staticmethod
    def get_procedure(
        db: Session,
        procedure_id: int,
    ):
        procedure = ProcedureRepository.get_by_id(
            db,
            procedure_id,
        )

        if not procedure:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Procedure not found",
            )

        return procedure

    @staticmethod
    def get_patient_procedures(
        db: Session,
        patient_id: int,
    ):
        return ProcedureRepository.get_by_patient(
            db,
            patient_id,
        )

    @staticmethod
    def update_procedure(
        db: Session,
        procedure_id: int,
        procedure_data: ProcedureUpdate,
    ):
        procedure = ProcedureRepository.get_by_id(
            db,
            procedure_id,
        )

        if not procedure:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Procedure not found",
            )

        return ProcedureRepository.update(
            db,
            procedure,
            procedure_data,
        )

    @staticmethod
    def delete_procedure(
        db: Session,
        procedure_id: int,
    ):
        procedure = ProcedureRepository.get_by_id(
            db,
            procedure_id,
        )

        if not procedure:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Procedure not found",
            )

        ProcedureRepository.delete(
            db,
            procedure,
        )