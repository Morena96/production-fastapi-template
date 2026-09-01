from fastapi import APIRouter

from app.services.tasks import example_job

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("/example")
async def queue_example(value: int):
    task = example_job.delay(value)
    return {"task_id": task.id, "status": "queued"}
