from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import sys
sys.path.append('..')
from app import crud, schemas, models, auth
from app.database import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[schemas.Task])
def get_tasks(
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    tasks = crud.get_tasks(db, user_id=current_user.id, skip=skip, limit=limit)
    return tasks

@router.post("/", response_model=schemas.Task)
def create_task(
    task: schemas.TaskCreate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    return crud.create_task(db=db, task=task, user_id=current_user.id)

@router.get("/{task_id}", response_model=schemas.Task)
def get_task(
    task_id: int,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    task = crud.get_task(db, task_id=task_id, user_id=current_user.id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    task = crud.update_task(db, task_id=task_id, task_update=task_update, user_id=current_user.id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    task = crud.delete_task(db, task_id=task_id, user_id=current_user.id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}