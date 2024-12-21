"""
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model Ingredient {
  id        Int      @id @default(autoincrement())
  name      String
  quantity  Int
  unit      String
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

"""
from fastapi import Depends
from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Annotated
from .ingredients import *


DB_URL = 'sqlite:///./test.sqlite3'
engine = create_engine(DB_URL)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

def init_db():
    # Create the database
    SQLModel.metadata.create_all(engine)




DATABASE = Annotated[Session, Depends(get_db)]