from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.procedure import (
    ProcedureCreate,
    ProcedureResponse,
    ProcedureUpdate,
)
from app.services.procedure_service import ProcedureService


router = APIRouter(
    prefix="/procedures",
    tags=["Procedures"],
)


@router.post(
    "/",
    response_model=ProcedureResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_procedure(
    procedure_data: ProcedureCreate,
    db: Session = Depends(get_db),
):
    return ProcedureService.create_procedure(
        db,
        procedure_data,
    )


@router.get(
    "/patient/{patient_id}",
    response_model=list[ProcedureResponse],
)
def get_patient_procedures(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return ProcedureService.get_patient_procedures(
        db,
        patient_id,
    )


@router.get(
    "/{procedure_id}",
    response_model=ProcedureResponse,
)
def get_procedure(
    procedure_id: int,
    db: Session = Depends(get_db),
):
    return ProcedureService.get_procedure(
        db,
        procedure_id,
    )


@router.patch(
    "/{procedure_id}",
    response_model=ProcedureResponse,
)
def update_procedure(
    procedure_id: int,
    procedure_data: ProcedureUpdate,
    db: Session = Depends(get_db),
):
    return ProcedureService.update_procedure(
        db,
        procedure_id,
        procedure_data,
    )


@router.delete(
    "/{procedure_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_procedure(
    procedure_id: int,
    db: Session = Depends(get_db),
):
    ProcedureService.delete_procedure(
        db,
        procedure_id,
    )