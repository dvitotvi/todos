from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()
todos = []

class Todo(BaseModel):
    id: str = None
    title: str
    completed: bool = False

@app.get("/todos")
def get_todos() -> List[Todo]:
    return todos

@app.post("/todos")
def create_todo(todo: Todo) -> Todo:
    todo.id = str(uuid.uuid4())
    todos.append(todo)
    return todo