from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token
from app.db.session import get_db
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse
from app.schemas.user import UserResponse
from app.services.users import authenticate, create_user, get_user_by_email

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(payload: RegisterRequest, db: Annotated[AsyncSession, Depends(get_db)]):
    if await get_user_by_email(db, payload.email):
        raise HTTPException(status_code=409, detail="Email already registered")
    return await create_user(db, payload.email, payload.password)


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, db: Annotated[AsyncSession, Depends(get_db)]):
    user = await authenticate(db, payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return TokenResponse(access_token=create_access_token(str(user.id), user.role))
