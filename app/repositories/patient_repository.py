from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.schemas.patient import PatientCreate


class PatientRepository:

    @staticmethod
    def create(
        db: Session,
        patient_data: PatientCreate
    ) -> Patient:

        patient = Patient(
            first_name=patient_data.first_name,
            last_name=patient_data.last_name,
            date_of_birth=patient_data.date_of_birth,
            gender=patient_data.gender,
            phone=patient_data.phone,
            email=patient_data.email,
            address=patient_data.address,
        )

        db.add(patient)
        db.commit()
        db.refresh(patient)

        return patient

    @staticmethod
    def get_by_id(
        db: Session,
        patient_id: int
    ) -> Patient | None:

        return db.get(Patient, patient_id)
    
    @staticmethod
    def update(
        db: Session,
        patient: Patient,
        patient_data: PatientUpdate
    ) -> Patient:

        update_data = patient_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(patient, field, value)

        db.commit()
        db.refresh(patient)

        return patient
    @staticmethod
    def delete(
        db: Session,
        patient: Patient
    ) -> None:

        db.delete(patient)
        db.commit()
