from sqlalchemy.orm import Session

from app.models.patient_doctor import PatientDoctor


class PatientDoctorRepository:

    @staticmethod
    def create(
        db: Session,
        patient_id: int,
        doctor_id: int
    ):
        patient_doctor = PatientDoctor(
            patient_id=patient_id,
            doctor_id=doctor_id,
            status="active"
        )

        db.add(patient_doctor)
        db.commit()
        db.refresh(patient_doctor)

        return patient_doctor

    @staticmethod
    def get_by_patient(
        db: Session,
        patient_id: int
    ):
        return (
            db.query(PatientDoctor)
            .filter(PatientDoctor.patient_id == patient_id)
            .all()
        )

    @staticmethod
    def get_by_doctor(
        db: Session,
        doctor_id: int
    ):
        return (
            db.query(PatientDoctor)
            .filter(PatientDoctor.doctor_id == doctor_id)
            .all()
        )

    @staticmethod
    def get_assignment(
        db: Session,
        patient_id: int,
        doctor_id: int
    ):
        return (
            db.query(PatientDoctor)
            .filter(
                PatientDoctor.patient_id == patient_id,
                PatientDoctor.doctor_id == doctor_id
            )
            .first()
        )

    @staticmethod
    def update_status(
        db: Session,
        assignment: PatientDoctor,
        status: str
    ):
        assignment.status = status

        db.commit()
        db.refresh(assignment)

        return assignment

    @staticmethod
    def delete(
        db: Session,
        assignment: PatientDoctor
    ):
        db.delete(assignment)
        db.commit()