from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.routes.medical_condition_routes import router as medical_condition_router
from app.core.database import get_db
from app.routes.patient_routes import router as patient_router
from app.routes.medical_report_routes import router as medical_report_router
from app.routes.allergy_routes import router as allergy_router
from app.routes.medication_routes import router as medication_router
from app.routes.procedure_routes import router as procedure_router
from app.routes.family_history_routes import router as family_history_router
from app.routes.patient_doctor_routes import router as patient_doctor_router
from app.routes.doctor_routes import router as doctor_router
from app.routes.auth_routes import router as auth_router
from app.routes.consultation_routes import (
    router as consultation_router,
)
from app.routes.medical_history_routes import (
    router as medical_history_router,
)




app = FastAPI(
    title="Healthcare Platform API",
    version="1.0.0"
)


app.include_router(patient_router)


@app.get("/")
def root():
    return {
        "message": "Healthcare Platform API is running"
    }


@app.get("/db-test")
def database_test(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))

    return {
        "database": result.scalar()
    }
app.include_router(medical_report_router)
app.include_router(medical_condition_router)
app.include_router(allergy_router)
app.include_router(medication_router)
app.include_router(procedure_router)
app.include_router(family_history_router)
app.include_router(medical_history_router)
app.include_router(doctor_router)
app.include_router(consultation_router)
app.include_router(auth_router)
app.include_router(patient_doctor_router)