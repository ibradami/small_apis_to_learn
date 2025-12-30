from fastapi import FastAPI, Path, HTTPException, Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

tasks=dict()

class Task(BaseModel):
    title: str
    completed: bool

class UpdateTask(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

@app.post("/todos/{id}")
def add_task(id: int = Path(..., description="Enter id of the task", gt=0), 
             task: Task = Body(...)):
    
    if id in tasks:
        raise HTTPException(status_code=409, detail="Task with such already exist")
    tasks[id]=task.model_dump()
    return {"message":"Task created", "task":tasks[id]}

@app.get("/todos")
def show_tasks():
    return tasks

@app.get("/todos/{id}")
def show_task(id: int = Path(...,description="Enter the id of the task that you want to view", gt=0)):
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[id]

@app.put("/todos/{id}")
def update_task(*, id: int = Path(..., description="Enter the id of the task that you want to edit", gt=0), 
                   task: UpdateTask= Body(...)):
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    stored_data=tasks[id]
    update_data=task.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        stored_data[key]=value
    return stored_data

@app.delete("/todos/{id}")
def delete_task(*, id: int = Path(..., description="Enter the id of the task that you want to delete", gt=0)):
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Such task already do not exist")
    del tasks[id]
    return {"message":"Task deleted"}