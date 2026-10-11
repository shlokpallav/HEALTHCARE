from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PatientDoctorCreate(BaseModel):
    patient_id: int
    doctor_id: int


class PatientDoctorStatusUpdate(BaseModel):
    status: str


class PatientDoctorResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    status: str
    assigned_at: datetime

    model_config = ConfigDict(from_attributes=True)