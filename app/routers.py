from .models import User, UserModel, db
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi import FastAPI

def router(app:FastAPI):
    router = SQLAlchemyCRUDRouter(User, UserModel, db)
    app.include_router(router)
    return app