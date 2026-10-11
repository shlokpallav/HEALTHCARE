from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.medication import (
    MedicationCreate,
    MedicationResponse,
    MedicationUpdate,
)
from app.services.medication_service import MedicationService


router = APIRouter(
    prefix="/medications",
    tags=["Medications"],
)


@router.post(
    "/",
    response_model=MedicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_medication(
    medication_data: MedicationCreate,
    db: Session = Depends(get_db),
):
    return MedicationService.create_medication(
        db,
        medication_data,
    )


@router.get(
    "/patient/{patient_id}",
    response_model=list[MedicationResponse],
)
def get_patient_medications(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return MedicationService.get_patient_medications(
        db,
        patient_id,
    )


@router.get(
    "/{medication_id}",
    response_model=MedicationResponse,
)
def get_medication(
    medication_id: int,
    db: Session = Depends(get_db),
):
    return MedicationService.get_medication(
        db,
        medication_id,
    )


@router.patch(
    "/{medication_id}",
    response_model=MedicationResponse,
)
def update_medication(
    medication_id: int,
    medication_data: MedicationUpdate,
    db: Session = Depends(get_db),
):
    return MedicationService.update_medication(
        db,
        medication_id,
        medication_data,
    )


@router.delete(
    "/{medication_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_medication(
    medication_id: int,
    db: Session = Depends(get_db),
):
    MedicationService.delete_medication(
        db,
        medication_id,
    )