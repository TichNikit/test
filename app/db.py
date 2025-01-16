from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_async_engine("postgresql+asyncpg://postgres:password@localhost/planes")

SessionLocal = async_sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Planes(Base):
    __tablename__ = 'planes'
    id: Mapped[int] = mapped_column(primary_key=True)
    flightid: Mapped[int] = mapped_column(unique=True)
    reg: Mapped[str]


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
