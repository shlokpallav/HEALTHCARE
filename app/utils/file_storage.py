import os
from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile, status


UPLOAD_DIR = Path("uploads/medical_reports")
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}

ALLOWED_CONTENT_TYPES = {
    ".pdf": {"application/pdf"},
    ".jpg": {"image/jpeg"},
    ".jpeg": {"image/jpeg"},
    ".png": {"image/png"},
}


async def save_medical_report(file: UploadFile) -> str:
    extension = Path(file.filename or "").suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF, JPG, JPEG and PNG files are allowed",
        )

    if file.content_type not in ALLOWED_CONTENT_TYPES[extension]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File type does not match the allowed format",
        )

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    filename = f"{uuid4().hex}{extension}"
    file_path = UPLOAD_DIR / filename
    size = 0

    try:
        with file_path.open("xb") as destination:
            while chunk := await file.read(1024 * 1024):
                size += len(chunk)

                if size > MAX_FILE_SIZE:
                    raise HTTPException(
                        status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                        detail="File size must not exceed 10 MB",
                    )

                destination.write(chunk)

        if size == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Uploaded file is empty",
            )

        return file_path.as_posix()

    except Exception:
        if file_path.exists():
            os.remove(file_path)

        raise

    finally:
        await file.close()