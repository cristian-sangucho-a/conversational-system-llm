from fastapi import FastAPI
from .routers.chat_router import chat_router

app = FastAPI(
    title="My API",
    description="conversacional bot via audio/text",
    version="0.1",
)

@app.get("/")
def read_root():
    """Root endpoint"""
    return {"Hello": "World"}

app.include_router(chat_router, prefix="/chat")