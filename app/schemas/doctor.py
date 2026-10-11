from pydantic import BaseModel, ConfigDict


class DoctorCreate(BaseModel):
    first_name: str
    last_name: str
    specialization: str
    phone: str | None = None
    email: str
    license_number: str
    clinic_name: str | None = None
    address: str | None = None


class DoctorUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    specialization: str | None = None
    phone: str | None = None
    email: str | None = None
    license_number: str | None = None
    clinic_name: str | None = None
    address: str | None = None


class DoctorResponse(BaseModel):
    doctor_id: int
    first_name: str
    last_name: str
    specialization: str
    phone: str | None
    email: str
    license_number: str
    clinic_name: str | None
    address: str | None

    model_config = ConfigDict(from_attributes=True)