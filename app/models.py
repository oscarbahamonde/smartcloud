from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
import os
import dotenv
from sqlmodel import create_engine, SQLModel, Session

dotenv.load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

engine = create_engine(DATABASE_URL)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

class User(SQLModel):
    displayName:str = Field(...)
    s_id:str = Field(...)
    photoURL:Optional[str]=Field()
    email:EmailStr = Field(...)
    
class Product(SQLModel):
    name:str=Field(...)
    price:float=Field(...)
    lab:Optional[str]=Field()
    description:str=Field(...)
    s_id:str=Field(...)
    photoURL:Optional[str]=Field()
    
class Users(User, table=True):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    created_at:datetime = Field(default_factory=datetime.now)

class Products(Product, table=True):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    created_at:datetime = Field(default_factory=datetime.now)