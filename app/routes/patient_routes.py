from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.patient import PatientCreate, PatientResponse, PatientUpdate
from app.services.patient_service import PatientService


router = APIRouter(
    prefix="/api/v1/patients",
    tags=["Patients"]
)


@router.post(
    "",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED
)
def create_patient(
    patient_data: PatientCreate,
    db: Session = Depends(get_db)
):
    return PatientService.create_patient(
        db,
        patient_data
    )
@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    return PatientService.get_patient(
        db,
        patient_id
    )
    
@router.patch(
    "/{patient_id}",
    response_model=PatientResponse
)
def update_patient(
    patient_id: int,
    patient_data: PatientUpdate,
    db: Session = Depends(get_db)
):
    return PatientService.update_patient(
        db,
        patient_id,
        patient_data
    )
@router.delete(
    "/{patient_id}",
    status_code=status.HTTP_200_OK
)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    return PatientService.delete_patient(
        db,
        patient_id
    )