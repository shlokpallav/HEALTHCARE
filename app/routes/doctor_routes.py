from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.doctor import (
    DoctorCreate,
    DoctorResponse,
    DoctorUpdate,
)
from app.services.doctor_service import DoctorService


router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"],
)


@router.post(
    "/",
    response_model=DoctorResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_doctor(
    doctor_data: DoctorCreate,
    db: Session = Depends(get_db),
):
    return DoctorService.create_doctor(
        db,
        doctor_data,
    )


@router.get(
    "/",
    response_model=list[DoctorResponse],
)
def get_all_doctors(
    db: Session = Depends(get_db),
):
    return DoctorService.get_all_doctors(db)


@router.get(
    "/{doctor_id}",
    response_model=DoctorResponse,
)
def get_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    return DoctorService.get_doctor(
        db,
        doctor_id,
    )


@router.patch(
    "/{doctor_id}",
    response_model=DoctorResponse,
)
def update_doctor(
    doctor_id: int,
    doctor_data: DoctorUpdate,
    db: Session = Depends(get_db),
):
    return DoctorService.update_doctor(
        db,
        doctor_id,
        doctor_data,
    )


@router.delete(
    "/{doctor_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    DoctorService.delete_doctor(
        db,
        doctor_id,
    )