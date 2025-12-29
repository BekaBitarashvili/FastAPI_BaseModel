from fastapi import FastAPI
from .routers import users_router
from .database import create_db_and_tables

app = FastAPI(title="My Professional API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users_router, prefix="/users", tags=["Users"])