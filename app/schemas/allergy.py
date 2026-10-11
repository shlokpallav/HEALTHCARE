from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class AllergyBase(BaseModel):
    allergy_name: str
    allergy_type: str | None = None
    reaction: str | None = None
    severity: str | None = None
    diagnosed_date: date | None = None
    source_report_id: int | None = None


class AllergyCreate(AllergyBase):
    patient_id: int


class AllergyUpdate(BaseModel):
    allergy_name: str | None = None
    allergy_type: str | None = None
    reaction: str | None = None
    severity: str | None = None
    diagnosed_date: date | None = None
    source_report_id: int | None = None
    status: str | None = None


class AllergyResponse(AllergyBase):
    model_config = ConfigDict(from_attributes=True)

    allergy_id: int
    patient_id: int
    status: str
    created_at: datetime
    updated_at: datetime