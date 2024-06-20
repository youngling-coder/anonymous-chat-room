from fastapi import FastAPI
from .routers import user, message, auth


app = FastAPI()

app.include_router(user.router, prefix="/users")
app.include_router(message.router, prefix="/messages")
app.include_router(auth.router, prefix="/auth")
