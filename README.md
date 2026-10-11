# Healthcare Platform API

A RESTful Healthcare Platform API built with **FastAPI, Python, SQLAlchemy, and PostgreSQL**. The project provides backend services for managing patient information, medical records, doctor assignments, consultations, and authentication.

## Features

- **Patient Management** — Create, retrieve, update, and manage patient records.
- **Medical Reports** — Manage report metadata and upload/download medical report files.
- **Medical Conditions** — Maintain patient medical condition records.
- **Allergies Management** — Store and manage patient allergy information.
- **Medications** — Manage medication records.
- **Procedures** — Maintain medical procedure information.
- **Family Medical History** — Store family medical history records.
- **Medical History Summary** — Retrieve a patient's consolidated medical history.
- **Doctor Management** — Manage doctor information.
- **Consultations** — Manage patient consultations.
- **Patient–Doctor Assignment** — Associate patients with doctors.
- **Authentication & Authorization** — User registration, login, JWT-based authentication, and role-based access control.

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Database Migrations:** Alembic
- **Authentication:** JWT
- **Password Hashing:** bcrypt
- **API Documentation:** Swagger UI / OpenAPI
- **File Uploads:** FastAPI UploadFile

## Project Structure

```text
HealtchCare/
├── alembic/
├── app/
│   ├── core/
│   ├── models/
│   ├── repositories/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   └── utils/
├── uploads/
├── alembic.ini
├── requirements.txt
└── run.py
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shlokpallav/HEALTHCARE.git
cd HEALTHCARE
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and configure your database connection and authentication settings.

```env
DATABASE_URL=your_postgresql_database_url
JWT_SECRET_KEY=your_secure_secret_key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
```

**Important:** Use your own credentials and a strong, randomly generated JWT secret. Never commit `.env` to GitHub.

### 5. Run Database Migrations

```bash
alembic upgrade head
```

Ensure your PostgreSQL database is created and accessible before running migrations.

### 6. Start the API

```bash
uvicorn app.main:app --reload
```

If your application entry point differs, use the appropriate module path for your project.

## API Documentation

After starting the server, open:

- **Swagger UI:** `http://127.0.0.1:8000/docs`
- **ReDoc:** `http://127.0.0.1:8000/redoc`

Use Swagger UI to explore and test the available API endpoints.

## Security Notes

- Keep database credentials and JWT secrets out of source control.
- Medical reports contain sensitive information and should be protected with appropriate access controls.
- Configure private, persistent file storage before production deployment.
- Use HTTPS and production-ready environment configuration when deploying.

## Future Improvements

- Cloud-based medical report storage
- Automated testing and API validation
- Production deployment and monitoring
- Enhanced medical report processing and data extraction

## Author

**Shlok Pallav**

GitHub: [shlokpallav](https://github.com/shlokpallav)

---

This project is being developed as a backend-focused healthcare management platform using modern Python API technologies.
