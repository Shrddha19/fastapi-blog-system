from fastapi import FastAPI
from fastapi .staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from route import routes
from database import base,engine
from models.table import shr
base.metadata.create_all(bind=engine)

happy=FastAPI()
happy.add_middleware(
    SessionMiddleware  , secret_key="shradha16"
)
happy.mount("/static",StaticFiles(directory="static"),name="static")


happy.include_router(routes.app)
