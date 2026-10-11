from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.consultation import (
    ConsultationCreate,
    ConsultationResponse,
    ConsultationUpdate,
)
from app.services.consultation_service import ConsultationService


router = APIRouter(
    prefix="/consultations",
    tags=["Consultations"],
)


@router.post(
    "/",
    response_model=ConsultationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_consultation(
    consultation_data: ConsultationCreate,
    db: Session = Depends(get_db),
):
    return ConsultationService.create_consultation(
        db,
        consultation_data,
    )


@router.get(
    "/patient/{patient_id}",
    response_model=list[ConsultationResponse],
)
def get_patient_consultations(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return ConsultationService.get_patient_consultations(
        db,
        patient_id,
    )


@router.get(
    "/doctor/{doctor_id}",
    response_model=list[ConsultationResponse],
)
def get_doctor_consultations(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    return ConsultationService.get_doctor_consultations(
        db,
        doctor_id,
    )


@router.get(
    "/{consultation_id}",
    response_model=ConsultationResponse,
)
def get_consultation(
    consultation_id: int,
    db: Session = Depends(get_db),
):
    return ConsultationService.get_consultation(
        db,
        consultation_id,
    )


@router.patch(
    "/{consultation_id}",
    response_model=ConsultationResponse,
)
def update_consultation(
    consultation_id: int,
    consultation_data: ConsultationUpdate,
    db: Session = Depends(get_db),
):
    return ConsultationService.update_consultation(
        db,
        consultation_id,
        consultation_data,
    )


@router.delete(
    "/{consultation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_consultation(
    consultation_id: int,
    db: Session = Depends(get_db),
):
    ConsultationService.delete_consultation(
        db,
        consultation_id,
    )