from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.medical_condition import (
    MedicalConditionCreate,
    MedicalConditionResponse,
    MedicalConditionUpdate,
)
from app.services.medical_condition_service import (
    MedicalConditionService,
)

router = APIRouter(
    prefix="/medical-conditions",
    tags=["Medical Conditions"],
)


@router.post(
    "/",
    response_model=MedicalConditionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_condition(
    condition_data: MedicalConditionCreate,
    db: Session = Depends(get_db),
):
    return MedicalConditionService.create_condition(
        db,
        condition_data,
    )


@router.get(
    "/{condition_id}",
    response_model=MedicalConditionResponse,
)
def get_condition(
    condition_id: int,
    db: Session = Depends(get_db),
):
    return MedicalConditionService.get_condition(
        db,
        condition_id,
    )


@router.get(
    "/patient/{patient_id}",
    response_model=list[MedicalConditionResponse],
)
def get_patient_conditions(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return MedicalConditionService.get_patient_conditions(
        db,
        patient_id,
    )


@router.patch(
    "/{condition_id}",
    response_model=MedicalConditionResponse,
)
def update_condition(
    condition_id: int,
    condition_data: MedicalConditionUpdate,
    db: Session = Depends(get_db),
):
    return MedicalConditionService.update_condition(
        db,
        condition_id,
        condition_data,
    )


@router.delete(
    "/{condition_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_condition(
    condition_id: int,
    db: Session = Depends(get_db),
):
    MedicalConditionService.delete_condition(
        db,
        condition_id,
    )