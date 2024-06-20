from datetime import datetime, timedelta
from datetime import UTC

from . import schemas, models
from .database import get_db
from .config import settings

from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = settings.jwt_secret_key
ALGORITHM = settings.jwt_algo
ACCESS_TOKEN_EXPIRATION_TIME = settings.jwt_expiration_time


def create_access_token(data: dict):

    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRATION_TIME)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_access_token(token: str, credentials_exception):

    try:
        payload = jwt.decode(token=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        id = str(payload.get("id"))

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)

    except:

        raise credentials_exception

    return token_data


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_402_PAYMENT_REQUIRED,
        detail=f"Could not validate credentials!",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = verify_access_token(
        token=token, credentials_exception=credentials_exception
    )
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user
