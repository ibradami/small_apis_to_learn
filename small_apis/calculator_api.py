from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/add")
def add(a: int = Query(..., description="First Number"),
        b: int = Query(..., description="Second Number")):
    return {"result":a+b}

@app.get("/subtract/{a}/{b}") # Aware of tradition to use either only Path or Query across specific API ( Just were trying :) )
def subtract(a: int = Path(..., description="First Number"), 
              b: int = Path(..., description="Second Number")):
    return {"result":a-b}

@app.get("/multiply")
def multiply(a: int = Query(..., description="First Number"),
            b: int = Query(..., description="Second Number")):
    return {"result":a*b}

@app.get("/divide")
def divide(a: int = Query(..., description="First Number"),
           b: int = Query(..., gt=0, description="Second Number")):
    return {"result":a/b}
