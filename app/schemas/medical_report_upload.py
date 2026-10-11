from pydantic import BaseModel


class MedicalReportUploadResponse(BaseModel):
    message: str
    file_path: str
    original_filename: str