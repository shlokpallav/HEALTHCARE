from sqlalchemy.orm import Session

from app.models.medical_report import MedicalReport
from app.schemas.medical_report import (
    MedicalReportCreate,
    MedicalReportUpdate
)


class MedicalReportRepository:

    @staticmethod
    def create(
        db: Session,
        report_data: MedicalReportCreate
    ) -> MedicalReport:

        report = MedicalReport(
            patient_id=report_data.patient_id,
            report_name=report_data.report_name,
            report_type=report_data.report_type,
            report_date=report_data.report_date,
            file_url=report_data.file_url,
        )

        db.add(report)
        db.commit()
        db.refresh(report)

        return report

    @staticmethod
    def get_by_id(
        db: Session,
        report_id: int
    ) -> MedicalReport | None:

        return db.get(MedicalReport, report_id)

    @staticmethod
    def get_by_patient_id(
        db: Session,
        patient_id: int
    ) -> list[MedicalReport]:

        return (
            db.query(MedicalReport)
            .filter(
                MedicalReport.patient_id == patient_id
            )
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        report: MedicalReport,
        report_data: MedicalReportUpdate
    ) -> MedicalReport:

        update_data = report_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(report, field, value)

        db.commit()
        db.refresh(report)

        return report

    @staticmethod
    def delete(
        db: Session,
        report: MedicalReport
    ) -> None:

        db.delete(report)
        db.commit()
    @staticmethod
    def get_by_patient_id(
    db: Session,
    patient_id: int
) -> list[MedicalReport]:

     return (
        db.query(MedicalReport)
        .filter(MedicalReport.patient_id == patient_id)
        .order_by(MedicalReport.report_date.desc())
        .all()
    )