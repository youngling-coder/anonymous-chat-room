from fastapi import FastAPI
from .routers import user, message

app = FastAPI()

app.include_router(user.router, prefix="/user")
app.include_router(message.router, prefix="/message")
