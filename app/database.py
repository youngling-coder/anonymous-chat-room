from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

DATABASE_URL = f"postgresql://{settings.db_usr}:{settings.db_pwd}@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(DATABASE_URL)

local_session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
base = declarative_base()


def get_db():
    db = local_session()

    try:
        yield db
    finally:
        db.close()
