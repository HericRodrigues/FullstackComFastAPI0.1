from pydantic import BaseModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.models import Category  # Seu modelo SQLAlchemy


router = APIRouter()

class CategoryBase(BaseModel):
    name: str
    description: str | None = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True