from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import (
    UserRegister,
    UserLogin,
    TokenResponse,
)
from app.services.auth_service import AuthService
from app.utils.auth import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
)
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db),
):
    user = AuthService.register_user(
        db,
        user_data,
    )

    return {
        "message": "User registered successfully",
        "user_id": user.user_id,
        "email": user.email,
        "role": user.role,
    }


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db),
):
    return AuthService.login_user(
        db,
        user_data,
    )
    
@router.get("/me")
def get_current_user_info(
    current_user: dict = Depends(get_current_user),
):
    return current_user