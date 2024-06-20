from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas


router = APIRouter(tags=["Messages"])


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.MessageResponse
)
def create_post(message: schemas.CreateMessage, db: Session = Depends(get_db)):
    pass
