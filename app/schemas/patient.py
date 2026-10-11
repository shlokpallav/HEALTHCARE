from datetime import date

from pydantic import BaseModel, EmailStr


class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone: str
    email: EmailStr
    address: str


class PatientResponse(BaseModel):
    patient_id: int
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    phone: str
    email: EmailStr
    address: str

from typing import Optional


class PatientUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None