from sqlalchemy.orm import Session

from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate


class DoctorRepository:

    @staticmethod
    def create(db: Session, doctor_data: DoctorCreate):
        doctor = Doctor(**doctor_data.model_dump())

        db.add(doctor)
        db.commit()
        db.refresh(doctor)

        return doctor

    @staticmethod
    def get_by_id(db: Session, doctor_id: int):
        return (
            db.query(Doctor)
            .filter(Doctor.doctor_id == doctor_id)
            .first()
        )

    @staticmethod
    def get_all(db: Session):
        return (
            db.query(Doctor)
            .order_by(Doctor.doctor_id.desc())
            .all()
        )

    @staticmethod
    def update(
        db: Session,
        doctor: Doctor,
        doctor_data: DoctorUpdate,
    ):
        update_data = doctor_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(doctor, field, value)

        db.commit()
        db.refresh(doctor)

        return doctor

    @staticmethod
    def delete(db: Session, doctor: Doctor):
        db.delete(doctor)
        db.commit()