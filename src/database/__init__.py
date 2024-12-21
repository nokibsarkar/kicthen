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
from sqlmodel import SQLModel, Field
DB_URL = 'sqlite:///./test.sqlite3'
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

