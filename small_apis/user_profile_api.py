from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()

users={}

class User(BaseModel):
    username: str
    email: str
    age: int

@app.post("/users")
def create_user(user: User):
    if user.username in users:
        raise HTTPException(status_code=409, detail="User already exists")
    users[user.username]=user.model_dump()
    return {
        "message":"User succesfully created",
        "username":user.username
    }

@app.get("/users/{username}")
def get_user(username: str = Path(..., description="Username")):
    if username not in users:
        raise HTTPException(status_code=404, detail="User is not found")
    return users[username]

