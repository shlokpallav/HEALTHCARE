from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ConsultationCreate(BaseModel):
    patient_id: int
    doctor_id: int
    consultation_date: datetime | None = None
    symptoms: str | None = None
    diagnosis: str | None = None
    notes: str | None = None
    prescription: str | None = None
    follow_up_date: datetime | None = None


class ConsultationUpdate(BaseModel):
    consultation_date: datetime | None = None
    symptoms: str | None = None
    diagnosis: str | None = None
    notes: str | None = None
    prescription: str | None = None
    follow_up_date: datetime | None = None


class ConsultationResponse(BaseModel):
    consultation_id: int
    patient_id: int
    doctor_id: int
    consultation_date: datetime
    symptoms: str | None
    diagnosis: str | None
    notes: str | None
    prescription: str | None
    follow_up_date: datetime | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)