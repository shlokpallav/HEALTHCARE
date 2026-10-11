from datetime import date, datetime

from pydantic import BaseModel


class MedicalReportCreate(BaseModel):
    patient_id: int
    report_name: str
    report_type: str
    report_date: date
    file_url: str | None = None


class MedicalReportUpdate(BaseModel):
    report_name: str | None = None
    report_type: str | None = None
    report_date: date | None = None
    file_url: str | None = None


class MedicalReportResponse(BaseModel):
    report_id: int
    patient_id: int
    report_name: str
    report_type: str
    report_date: date
    file_url: str | None
    uploaded_at: datetime