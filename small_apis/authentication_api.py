from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import bcrypt

## Hashing Password
def hash_password(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password: str, hashed):
    return bcrypt.checkpw(password.encode(), hashed)

app = FastAPI()

class RegisterUser(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=3, max_length=20)
    email: str = Field()
    birthdate: str = Field()

class LoginUser(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=3, max_length=20)


users={}

@app.post("/register")
def create_user(user: RegisterUser = Body(...)):
    if user.username in users:
        raise HTTPException(status_code=409, detail="Username already taken")
    user_info=user.model_dump()
    user_info["password"]=hash_password(user.password)
    users[user_info["username"]]=user_info
    return {"message":"Success! User created"}

@app.post("/login")
def login_user(user: LoginUser = Body(...)):
    if user.username not in users:
        raise HTTPException(status_code=404, detail="Such user do not exist")
    if not verify_password(user.password, users[user.username]["password"]):
        raise HTTPException(status_code=401, detail="Wrong Password")
    return {"message":"Success! User logged in"}

