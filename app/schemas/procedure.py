from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class ProcedureCreate(BaseModel):
    patient_id: int
    procedure_name: str
    procedure_date: date | None = None
    reason: str | None = None
    hospital: str | None = None
    surgeon_or_doctor: str | None = None
    outcome: str | None = None
    status: str = "pending"
    source_report_id: int | None = None


class ProcedureUpdate(BaseModel):
    procedure_name: str | None = None
    procedure_date: date | None = None
    reason: str | None = None
    hospital: str | None = None
    surgeon_or_doctor: str | None = None
    outcome: str | None = None
    status: str | None = None
    source_report_id: int | None = None


class ProcedureResponse(BaseModel):
    procedure_id: int
    patient_id: int
    procedure_name: str
    procedure_date: date | None
    reason: str | None
    hospital: str | None
    surgeon_or_doctor: str | None
    outcome: str | None
    status: str
    source_report_id: int | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)