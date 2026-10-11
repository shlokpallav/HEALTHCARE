from datetime import date

from pydantic import BaseModel, ConfigDict

from app.schemas.medical_report import MedicalReportResponse
from app.schemas.medical_condition import MedicalConditionResponse
from app.schemas.allergy import AllergyResponse
from app.schemas.medication import MedicationResponse
from app.schemas.procedure import ProcedureResponse
from app.schemas.family_history import FamilyHistoryResponse


class PatientSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    patient_id: int
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone: str | None = None
    email: str | None = None
    address: str | None = None


class MedicalHistoryResponse(BaseModel):
    patient: PatientSummary
    medical_reports: list[MedicalReportResponse]
    medical_conditions: list[MedicalConditionResponse]
    allergies: list[AllergyResponse]
    medications: list[MedicationResponse]
    procedures: list[ProcedureResponse]
    family_history: list[FamilyHistoryResponse]