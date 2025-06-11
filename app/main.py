from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, auth
from .database import engine, get_db
from .routers import auth as auth_router, tasks as tasks_router


# Создаем таблицы в базе данных
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 
app.include_router(auth_router.router)
app.include_router(tasks_router.router)

 
try:
    app.mount("/static", StaticFiles(directory="frontend"), name="static")
except RuntimeError:
    pass  

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API"}

@app.get("/health")
def health_check():
    return {"status": "working", "database": "connected"}

 
@app.get("/me", response_model=schemas.User)
def get_current_user_info(current_user: models.User = Depends(auth.get_current_active_user)):
    return current_user

@app.post("/create_task", response_model=schemas.Task)
def create_user_task(
    task: schemas.TaskCreate,
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    from . import crud
    return crud.create_task(db=db, task=task, user_id=current_user.id)

@app.get("/get_tasks", response_model=list[schemas.Task])
def get_user_tasks(
    current_user: models.User = Depends(auth.get_current_active_user),
    db: Session = Depends(get_db)
):
    from . import crud
    return crud.get_tasks(db, user_id=current_user.id)