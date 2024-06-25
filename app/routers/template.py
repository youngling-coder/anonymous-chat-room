from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory=f"{BASE_DIR}/templates")

router = APIRouter(tags=["Templates"])


@router.get("/", response_class=HTMLResponse)
def index_page(request: Request):

    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/users/{username}", response_class=HTMLResponse)
def index_page(request: Request, username: str):

    return templates.TemplateResponse(
        "index.html", {"request": request, "username": username}
    )


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):

    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/signup", response_class=HTMLResponse)
def signup_page(request: Request):

    return templates.TemplateResponse("signup.html", {"request": request})


@router.get("/profile/{username}", response_class=HTMLResponse)
def profile_page(request: Request, username: str):

    return templates.TemplateResponse("profile.html", {"request": request, "username": username})