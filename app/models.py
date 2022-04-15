from sqlmodel import SQLModel, create_engine, Field
from sqlalchemy.orm import sessionmaker
from pydantic import EmailStr, HttpUrl 
from uuid import UUID, uuid4
from datetime import datetime
from os import getenv
from dotenv import load_dotenv
from typing import Optional
load_dotenv()

DB_URL = getenv("DB_URL")

class User(SQLModel):
    displayName:str = Field(...)
    photoURL:Optional[HttpUrl]=Field()
    email:EmailStr = Field(...)
    
class UserModel(User, table=True):
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