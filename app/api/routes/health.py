from fastapi import APIRouter
from sqlalchemy import text

from app.db.session import SessionLocal

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/live")
async def live():
    return {"status": "alive"}


@router.get("/ready")
async def ready():
    async with SessionLocal() as db:
        await db.execute(text("SELECT 1"))
    return {"status": "ready"}
