from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.patient_doctor import (
    PatientDoctorCreate,
    PatientDoctorResponse,
    PatientDoctorStatusUpdate,
)
from app.services.patient_doctor_service import PatientDoctorService


router = APIRouter(
    prefix="/patient-doctors",
    tags=["Patient Doctor"]
)


@router.post(
    "/",
    response_model=PatientDoctorResponse,
    status_code=status.HTTP_201_CREATED
)
def assign_doctor(
    data: PatientDoctorCreate,
    db: Session = Depends(get_db)
):
    return PatientDoctorService.assign_doctor(
        db,
        data.patient_id,
        data.doctor_id
    )


@router.get(
    "/patient/{patient_id}",
    response_model=list[PatientDoctorResponse]
)
def get_patient_doctors(
    patient_id: int,
    db: Session = Depends(get_db)
):
    return PatientDoctorService.get_patient_doctors(
        db,
        patient_id
    )


@router.get(
    "/doctor/{doctor_id}",
    response_model=list[PatientDoctorResponse]
)
def get_doctor_patients(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    return PatientDoctorService.get_doctor_patients(
        db,
        doctor_id
    )


@router.patch(
    "/patient/{patient_id}/doctor/{doctor_id}",
    response_model=PatientDoctorResponse
)
def update_assignment_status(
    patient_id: int,
    doctor_id: int,
    data: PatientDoctorStatusUpdate,
    db: Session = Depends(get_db)
):
    return PatientDoctorService.update_status(
        db,
        patient_id,
        doctor_id,
        data.status
    )


@router.delete(
    "/patient/{patient_id}/doctor/{doctor_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_assignment(
    patient_id: int,
    doctor_id: int,
    db: Session = Depends(get_db)
):
    PatientDoctorService.remove_assignment(
        db,
        patient_id,
        doctor_id
    )