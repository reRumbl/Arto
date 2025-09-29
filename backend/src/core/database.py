from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncAttrs
from src.core.utils import utc_now
from src.config import db_settings

# --- Engine ---
engine = create_async_engine(
    url=db_settings.asyncpg_url,
    pool_size=db_settings.DB_POOL_SIZE,
    max_overflow=db_settings.DB_MAX_OVERFLOW,
    echo=db_settings.DB_ECHO
)

# --- Session Factory ---
SessionFactory = async_sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)


# --- Base model class ---
class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True, unique=True)
    created_at: Mapped[datetime] = mapped_column(default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(default=utc_now, onupdate=utc_now)
