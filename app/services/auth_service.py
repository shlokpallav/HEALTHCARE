from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import bcrypt

from app.repositories.user_repository import UserRepository
from app.schemas.auth import UserRegister, UserLogin
from app.utils.security import create_access_token


class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        user_data: UserRegister,
    ):
        existing_user = UserRepository.get_by_email(
            db,
            user_data.email,
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        allowed_roles = {
            "patient",
            "doctor",
            "admin",
        }

        if user_data.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid role",
            )

        password_hash = bcrypt.hashpw(
            user_data.password.encode("utf-8"),
            bcrypt.gensalt(),
        ).decode("utf-8")

        return UserRepository.create(
            db,
            user_data.email,
            password_hash,
            user_data.role,
        )

    @staticmethod
    def login_user(
        db: Session,
        user_data: UserLogin,
    ):
        user = UserRepository.get_by_email(
            db,
            user_data.email,
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        password_valid = bcrypt.checkpw(
            user_data.password.encode("utf-8"),
            user.password_hash.encode("utf-8"),
        )

        if not password_valid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        access_token = create_access_token(
            {
                "sub": str(user.user_id),
                "role": user.role,
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer",
        }