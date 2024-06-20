from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, oauth2


router = APIRouter(tags=["Messages"])


@router.post(
    "/create", status_code=status.HTTP_201_CREATED, response_model=schemas.MessageResponse
)
def create_message(
    message: schemas.CreateMessage,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):

    new_message = models.Message(owner_id=current_user.id, **message.model_dump())

    db.add(new_message)
    db.commit()
    db.refresh(new_message)

    return new_message
