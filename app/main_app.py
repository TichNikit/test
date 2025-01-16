# uvicorn app.main_app:app --reload
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import create_table
from app.routers.router_plane import router_planes


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_table()
    print("База готова")
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router_planes)
