from fastapi import FastAPI
from routers import router as notes_router

app = FastAPI()
app.include_router(notes_router)
