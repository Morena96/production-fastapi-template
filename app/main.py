from fastapi import FastAPI

from app.api.routes import admin, auth, health, jobs, users
from app.core.config import settings

app = FastAPI(title=settings.app_name, version="1.0.0")
app.include_router(health.router)
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(admin.router, prefix="/api/v1")
app.include_router(jobs.router, prefix="/api/v1")
