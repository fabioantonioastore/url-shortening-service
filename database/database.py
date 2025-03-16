from dotenv import load_dotenv
from os import getenv

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

load_dotenv()

async_engine = create_async_engine(url=getenv("DATABASE_URL"), echo=False)

session_factory = async_sessionmaker(bind=async_engine, expire_on_commit=False)
