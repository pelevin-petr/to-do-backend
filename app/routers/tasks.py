from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from datetime import datetime
from app.db.models import Tasks
from app.db.connection import get_db
from app.routers.auth import get_current_user
from app.shemas.task import CreateTask, Task


task_router = APIRouter()


@task_router.post("/tasks", response_model=Task)
async def create_task(task: CreateTask, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    new_task = Tasks(
        title=task.title,
        status=task.status,
        description=task.description,
        created_at=datetime.now(),
        user_id=current_user.id
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task


@task_router.get("/tasks", response_model=List[Task])
async def get_tasks(db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    result = await db.execute(select(Tasks).filter(Tasks.user_id == current_user.id))
    tasks = result.scalars().all()
    return tasks


@task_router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    result = await db.execute(
        select(Tasks).filter(Tasks.id == task_id, Tasks.user_id == current_user.id)
    )
    task = result.scalars().first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@task_router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: CreateTask, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    result = await db.execute(
        select(Tasks).filter(Tasks.id == task_id, Tasks.user_id == current_user.id)
    )
    existing_task = result.scalars().first()

    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    existing_task.title = task.title
    existing_task.status = task.status
    existing_task.description = task.description

    await db.commit()
    await db.refresh(existing_task)
    return existing_task


@task_router.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    result = await db.execute(
        select(Tasks).filter(Tasks.id == task_id, Tasks.user_id == current_user.id)
    )
    task = result.scalars().first()

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    await db.delete(task)
    await db.commit()
    return {"detail": "Task deleted successfully"}
