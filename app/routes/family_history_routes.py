from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.family_history import (
    FamilyHistoryCreate,
    FamilyHistoryResponse,
    FamilyHistoryUpdate,
)
from app.services.family_history_service import FamilyHistoryService


router = APIRouter(
    prefix="/family-history",
    tags=["Family Medical History"],
)


@router.post(
    "/",
    response_model=FamilyHistoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_family_history(
    history_data: FamilyHistoryCreate,
    db: Session = Depends(get_db),
):
    return FamilyHistoryService.create_history(
        db,
        history_data,
    )


@router.get(
    "/patient/{patient_id}",
    response_model=list[FamilyHistoryResponse],
)
def get_patient_family_history(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return FamilyHistoryService.get_patient_history(
        db,
        patient_id,
    )


@router.get(
    "/{family_history_id}",
    response_model=FamilyHistoryResponse,
)
def get_family_history(
    family_history_id: int,
    db: Session = Depends(get_db),
):
    return FamilyHistoryService.get_history(
        db,
        family_history_id,
    )


@router.patch(
    "/{family_history_id}",
    response_model=FamilyHistoryResponse,
)
def update_family_history(
    family_history_id: int,
    history_data: FamilyHistoryUpdate,
    db: Session = Depends(get_db),
):
    return FamilyHistoryService.update_history(
        db,
        family_history_id,
        history_data,
    )


@router.delete(
    "/{family_history_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_family_history(
    family_history_id: int,
    db: Session = Depends(get_db),
):
    FamilyHistoryService.delete_history(
        db,
        family_history_id,
    )