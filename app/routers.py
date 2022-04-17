from .models import User, Users, db, Product, Products
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from fastapi import FastAPI, APIRouter

def router(app:FastAPI):
    router = SQLAlchemyCRUDRouter(User, Users, db)
    product=SQLAlchemyCRUDRouter(Product, Products, db)
    app.include_router(router)
    app.include_router(product)
    return app