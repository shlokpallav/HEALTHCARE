from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.medical_report import MedicalReport
from app.repositories.medical_report_repository import (
    MedicalReportRepository
)
from app.repositories.patient_repository import PatientRepository
from app.schemas.medical_report import (
    MedicalReportCreate,
    MedicalReportUpdate
)


class MedicalReportService:

    @staticmethod
    def create_report(
        db: Session,
        report_data: MedicalReportCreate
    ):
        patient = PatientRepository.get_by_id(
            db,
            report_data.patient_id
        )

        if patient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )

        return MedicalReportRepository.create(
            db,
            report_data
        )

    @staticmethod
    def get_report(
        db: Session,
        report_id: int
    ):
        report = MedicalReportRepository.get_by_id(
            db,
            report_id
        )

        if report is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medical report not found"
            )

        return report

    @staticmethod
    def get_patient_reports(
        db: Session,
        patient_id: int
    ):
        patient = PatientRepository.get_by_id(
            db,
            patient_id
        )

        if patient is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found"
            )

        return MedicalReportRepository.get_by_patient_id(
            db,
            patient_id
        )

    @staticmethod
    def update_report(
        db: Session,
        report_id: int,
        report_data: MedicalReportUpdate
    ):
        report = MedicalReportRepository.get_by_id(
            db,
            report_id
        )

        if report is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medical report not found"
            )

        return MedicalReportRepository.update(
            db,
            report,
            report_data
        )

    @staticmethod
    def delete_report(
        db: Session,
        report_id: int
    ):
        report = MedicalReportRepository.get_by_id(
            db,
            report_id
        )

        if report is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medical report not found"
            )

        MedicalReportRepository.delete(
            db,
            report
        )

        return {
            "message": "Medical report deleted successfully"
        }
    @staticmethod
    def get_patient_reports(
    db: Session,
    patient_id: int
) -> list[MedicalReport]:

      return MedicalReportRepository.get_by_patient_id(
        db,
        patient_id
    )