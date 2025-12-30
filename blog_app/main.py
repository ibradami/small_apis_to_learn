from fastapi import FastAPI
from routers import router as blog_router

app = FastAPI()
app.include_router(blog_router)