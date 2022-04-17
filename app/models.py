from sqlmodel import SQLModel, create_engine, Field
from sqlalchemy.orm import sessionmaker
from pydantic import EmailStr
from uuid import UUID, uuid4
from datetime import datetime
from os import getenv
from dotenv import load_dotenv
from typing import Optional
load_dotenv()

DB_URL = getenv("DB_URL")

class User(SQLModel):
    displayName:str = Field(...)
    s_id:str = Field(...)
    photoURL:Optional[str]=Field()
    email:EmailStr = Field(...)
    
class Users(User, table=True):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    created_at:datetime = Field(default_factory=datetime.utcnow)
    updated_at:datetime = Field(default_factory=datetime.utcnow)
    
class MediaFile(SQLModel):
    name:str=Field(...)
    typeof:str=Field(...)
    url:str=Field(...)
    s_id:str=Field(...)

class MediaFileModel(SQLModel):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    created_at:datetime = Field(default_factory=datetime.utcnow)
    updated_at:datetime = Field(default_factory=datetime.utcnow)
    uid:UUID=Field(..., foreign_key=Users.id)

class Product(SQLModel):
    name:str=Field(...)
    price:float=Field(...)
    lab:Optional[str]=Field()
    description:str=Field(...)
    s_id:str=Field(...)
    photoURL:Optional[str]=Field()
    
class Products(Product, table=True):
    id:UUID = Field(default_factory=uuid4, primary_key=True)
    created_at:datetime = Field(default_factory=datetime.utcnow)
    updated_at:datetime = Field(default_factory=datetime.utcnow)


SQLModel.metadata.create_all(bind=create_engine(DB_URL))
  
def db():
    sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=create_engine(DB_URL))
    session = sessionLocal()
    try:
        yield session
    finally:
        session.close()