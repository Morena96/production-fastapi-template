from celery import Celery

from app.core.config import settings

celery_app = Celery("app", broker=settings.redis_url, backend=settings.redis_url)


@celery_app.task(name="jobs.example")
def example_job(value: int) -> dict:
    return {"input": value, "result": value * 2}
