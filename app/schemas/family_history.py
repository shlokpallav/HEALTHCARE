from pydantic import BaseModel, ConfigDict


class FamilyHistoryCreate(BaseModel):
    patient_id: int
    relation: str
    condition_name: str
    diagnosed_age: int | None = None
    status: str = "confirmed"
    notes: str | None = None


class FamilyHistoryUpdate(BaseModel):
    relation: str | None = None
    condition_name: str | None = None
    diagnosed_age: int | None = None
    status: str | None = None
    notes: str | None = None


class FamilyHistoryResponse(BaseModel):
    family_history_id: int
    patient_id: int
    relation: str
    condition_name: str
    diagnosed_age: int | None
    status: str
    notes: str | None

    model_config = ConfigDict(from_attributes=True)