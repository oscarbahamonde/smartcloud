from fastapi import FastAPI, Depends
from sqlmodel import Session
from app.db import init_db, get_session
from app.models import Users, Products
from app.schemas import UserCreate, ProductCreate

app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()
    

@app.get('/users')
async def get_users(session: Session = Depends(get_session)):
    users = session.query(Users).all()
    return users

@app.get('/products')
async def get_products(session: Session = Depends(get_session)):
    products = session.query(Products).all()
    return products

@app.get('/users/{s_id}')
async def get_user(s_id: str, session: Session = Depends(get_session)):
    user = session.query(Users).filter(Users.s_id == s_id).first()
    return user
@app.get('/products/{s_id}')
async def get_products(s_id: str, session: Session = Depends(get_session)):
    product = session.query(Products).filter(Products.s_id == s_id).all()
    return product
@app.post('/users/{s_id}')
async def create_user(s_id: str, user: UserCreate, session: Session = Depends(get_session)):
    user = Users(s_id=s_id, displayName=user.displayName, photoURL=user.photoURL, email=user.email)
    session.add(user)
    session.commit()
    return user
@app.post('/products/{s_id}')
async def create_product(s_id: str, product: ProductCreate, session: Session = Depends(get_session)):
    product = Products(s_id=s_id, name=product.name, price=product.price, lab=product.lab, description=product.description, photoURL=product.photoURL)
    session.add(product)
    session.commit()
    return product 