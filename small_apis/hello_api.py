from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def get_message():
    return {"message":"Hello, World"}

@app.get("/health") # Constantly is used to check working of APIs
def check_health():
    return {"status":"ok"}