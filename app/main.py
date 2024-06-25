from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import user, message, auth, template

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

app.mount("/static", StaticFiles(directory=f"{BASE_DIR}/static"), name="static")

app.include_router(user.router, prefix="/users")
app.include_router(message.router, prefix="/messages")
app.include_router(auth.router, prefix="/auth")
app.include_router(template.router)
