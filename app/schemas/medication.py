from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class MedicationCreate(BaseModel):
    patient_id: int
    medicine_name: str
    dosage: str | None = None
    frequency: str | None = None
    route: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    reason: str | None = None
    prescribed_by: str | None = None
    source_report_id: int | None = None
    status: str = "pending"


class MedicationUpdate(BaseModel):
    medicine_name: str | None = None
    dosage: str | None = None
    frequency: str | None = None
    route: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    reason: str | None = None
    prescribed_by: str | None = None
    source_report_id: int | None = None
    status: str | None = None


class MedicationResponse(BaseModel):
    medication_id: int
    patient_id: int
    medicine_name: str
    dosage: str | None
    frequency: str | None
    route: str | None
    start_date: date | None
    end_date: date | None
    reason: str | None
    prescribed_by: str | None
    source_report_id: int | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)