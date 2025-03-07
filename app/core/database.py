import os
from dotenv import load_dotenv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)

Session = async_sessionmaker(engine, expire_on_commit=False)