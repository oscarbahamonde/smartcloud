from fastapi import FastAPI
from .server import server
from .routers import router
from .models import db

app = FastAPI()
db()
server(app)
router(app)
