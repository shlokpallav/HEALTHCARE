from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class MedicalConditionCreate(BaseModel):
    patient_id: int
    condition_name: str
    diagnosed_date: date | None = None
    source_report_id: int | None = None


class MedicalConditionUpdate(BaseModel):
    condition_name: str | None = None
    diagnosed_date: date | None = None
    source_report_id: int | None = None
    status: str | None = None


class MedicalConditionResponse(BaseModel):
    condition_id: int
    patient_id: int
    condition_name: str
    diagnosed_date: date | None
    source_report_id: int | None
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)