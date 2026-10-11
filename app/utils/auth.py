from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.security import decode_access_token


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    token = credentials.credentials

    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")
    role = payload.get("role")

    if not user_id or not role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "user_id": int(user_id),
        "role": role,
    }


def require_patient(
    current_user: dict = Depends(get_current_user),
):
    if current_user["role"] != "patient":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Patient access required",
        )

    return current_user


def require_doctor(
    current_user: dict = Depends(get_current_user),
):
    if current_user["role"] != "doctor":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Doctor access required",
        )

    return current_user


def require_admin(
    current_user: dict = Depends(get_current_user),
):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required",
        )

    return current_user