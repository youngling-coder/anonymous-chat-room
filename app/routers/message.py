from datetime import datetime

from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, models, oauth2


router = APIRouter(tags=["Messages"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.MessageResponse,
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


@router.get("/get_latest", response_model=list[schemas.MessageResponse])
def get_latest_messages(timestamp: str, db: Session = Depends(get_db), current_user=Depends(oauth2.get_current_user)):

    from_timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))

    messages = db.query(models.Message).filter(models.Message.timestamp >= from_timestamp).all()

    if not messages:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return messages