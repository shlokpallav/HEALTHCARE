from datetime import date
from pathlib import Path

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    UploadFile,
    status,
)
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.utils.auth import get_current_user
from app.core.database import get_db
from app.models.medical_report import MedicalReport
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.models.patient_doctor import PatientDoctor
from app.schemas.medical_report import (
    MedicalReportCreate,
    MedicalReportResponse,
    MedicalReportUpdate,
)
from app.services.medical_report_service import MedicalReportService
from app.utils.file_storage import save_medical_report


router = APIRouter(
    prefix="/api/v1/medical-reports",
    tags=["Medical Reports"],
)


@router.post(
    "",
    response_model=MedicalReportResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_report(
    report_data: MedicalReportCreate,
    db: Session = Depends(get_db),
):
    return MedicalReportService.create_report(db, report_data)


@router.post(
    "/upload",
    response_model=MedicalReportResponse,
    status_code=status.HTTP_201_CREATED,
)
async def upload_medical_report(
    patient_id: int = Form(...),
    report_name: str = Form(...),
    report_type: str = Form(...),
    report_date: date = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    file_path = await save_medical_report(file)

    report_data = MedicalReportCreate(
        patient_id=patient_id,
        report_name=report_name,
        report_type=report_type,
        report_date=report_date,
        file_url=file_path,
    )

    try:
        return MedicalReportService.create_report(db, report_data)
    except Exception:
        Path(file_path).unlink(missing_ok=True)
        raise


@router.get(
    "/patient/{patient_id}",
    response_model=list[MedicalReportResponse],
)
def get_patient_reports(
    patient_id: int,
    db: Session = Depends(get_db),
):
    return MedicalReportService.get_patient_reports(db, patient_id)


@router.get(
    "/{report_id}/download",
    response_class=FileResponse,
)
def download_medical_report(
    report_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    report = db.query(MedicalReport).filter(
        MedicalReport.report_id == report_id
    ).first()

    if report is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medical report not found",
        )

    role = current_user["role"]

    if role == "patient":
        patient = db.query(Patient).filter(
            Patient.user_id == current_user["user_id"]
        ).first()

        if patient is None or report.patient_id != patient.patient_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to access this report",
            )

    elif role == "doctor":
        doctor = db.query(Doctor).filter(
            Doctor.user_id == current_user["user_id"]
        ).first()

        if doctor is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Doctor profile not found",
            )

        assignment = db.query(PatientDoctor).filter(
            PatientDoctor.patient_id == report.patient_id,
            PatientDoctor.doctor_id == doctor.doctor_id,
            PatientDoctor.status == "active",
        ).first()

        if assignment is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not allowed to access this report",
            )

    elif role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    if not report.file_url:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No file is associated with this report",
        )

    file_path = Path(report.file_url).resolve()
    upload_root = Path("uploads/medical_reports").resolve()

    if not file_path.is_relative_to(upload_root):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid report file path",
        )

    if not file_path.is_file():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Medical report file not found on server",
        )

    return FileResponse(
        path=str(file_path),
        filename=file_path.name,
        media_type="application/octet-stream",
    )


@router.get(
    "/{report_id}",
    response_model=MedicalReportResponse,
)
def get_report(
    report_id: int,
    db: Session = Depends(get_db),
):
    return MedicalReportService.get_report(db, report_id)


@router.patch(
    "/{report_id}",
    response_model=MedicalReportResponse,
)
def update_report(
    report_id: int,
    report_data: MedicalReportUpdate,
    db: Session = Depends(get_db),
):
    return MedicalReportService.update_report(
        db, report_id, report_data
    )


@router.delete(
    "/{report_id}",
    status_code=status.HTTP_200_OK,
)
def delete_report(
    report_id: int,
    db: Session = Depends(get_db),
):
    return MedicalReportService.delete_report(db, report_id)