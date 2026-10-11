from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.allergy import (
    AllergyCreate,
    AllergyResponse,
    AllergyUpdate,
)
from app.services.allergy_service import AllergyService


router = APIRouter(
    prefix="/allergies",
    tags=["Allergies"],
)


@router.post(
    "/",
    response_model=AllergyResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_allergy(
    allergy_data: AllergyCreate,
    db: Session = Depends(get_db),
):
    return AllergyService.create_allergy(
        db,
        allergy_data,
    )


@router.get(
    "/patient/{patient_id}",
    response_model=list[AllergyResponse],
)
def get_patient_allergies(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return AllergyService.get_patient_allergies(
        db,
        patient_id,
    )


@router.get(
    "/{allergy_id}",
    response_model=AllergyResponse,
)
def get_allergy(
    allergy_id: int,
    db: Session = Depends(get_db),
):
    return AllergyService.get_allergy(
        db,
        allergy_id,
    )


@router.patch(
    "/{allergy_id}",
    response_model=AllergyResponse,
)
def update_allergy(
    allergy_id: int,
    allergy_data: AllergyUpdate,
    db: Session = Depends(get_db),
):
    return AllergyService.update_allergy(
        db,
        allergy_id,
        allergy_data,
    )


@router.delete(
    "/{allergy_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_allergy(
    allergy_id: int,
    db: Session = Depends(get_db),
):
    AllergyService.delete_allergy(
        db,
        allergy_id,
    )