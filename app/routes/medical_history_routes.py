from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.utils.auth import require_patient
from app.core.database import get_db
from app.schemas.medical_history import MedicalHistoryResponse
from app.services.medical_history_service import MedicalHistoryService


router = APIRouter(
    prefix="/medical-history",
    tags=["Medical History"],
)


@router.get(
    "/patient/{patient_id}",
    response_model=MedicalHistoryResponse,
)
def get_patient_medical_history(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return MedicalHistoryService.get_patient_medical_history(
        db,
        patient_id,
    )
@router.get("/patient/{patient_id}", response_model=MedicalHistoryResponse)
def get_patient_medical_history(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(require_patient)
):
    if current_user["user_id"] != patient_id:
        raise HTTPException(
            status_code=403,
            detail="You can only access your own medical history"
        )

    return MedicalHistoryService.get_patient_medical_history(
        db,
        patient_id
    )