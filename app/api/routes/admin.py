from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.deps import require_role
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/stats")
async def stats(_: Annotated[User, Depends(require_role("admin"))]):
    return {"status": "ok", "scope": "admin"}
