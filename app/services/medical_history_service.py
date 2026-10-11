from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.medical_history import PatientSummary
from app.models.patient import Patient

from app.repositories.medical_report_repository import (
    MedicalReportRepository,
)
from app.repositories.medical_condition_repository import (
    MedicalConditionRepository,
)
from app.repositories.allergy_repository import (
    AllergyRepository,
)
from app.repositories.medication_repository import (
    MedicationRepository,
)
from app.repositories.procedure_repository import (
    ProcedureRepository,
)
from app.repositories.family_history_repository import (
    FamilyHistoryRepository,
)


class MedicalHistoryService:

    @staticmethod
    def get_patient_medical_history(
        db: Session,
        patient_id: int,
    ):
        patient = (
            db.query(Patient)
            .filter(Patient.patient_id == patient_id)
            .first()
        )

        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient not found",
            )

        return {
            "patient": PatientSummary.model_validate(patient),

            "medical_reports":
                MedicalReportRepository.get_by_patient_id(
                    db,
                    patient_id,
                ),

            "medical_conditions":
                MedicalConditionRepository.get_by_patient_id(
                    db,
                    patient_id,
                ),

            "allergies":
                AllergyRepository.get_by_patient(
                    db,
                    patient_id,
                ),

            "medications":
                MedicationRepository.get_by_patient(
                    db,
                    patient_id,
                ),

            "procedures":
                ProcedureRepository.get_by_patient(
                    db,
                    patient_id,
                ),

            "family_history":
                FamilyHistoryRepository.get_by_patient(
                    db,
                    patient_id,
                ),
        }