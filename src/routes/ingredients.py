from fastapi import APIRouter
from typing import Generic, TypeVar, Any, List
from sqlmodel import SQLModel
from ..database import DATABASE, IngredientCreate, Ingredient
ingredients_router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
    responses={404: {"description": "Not found"}},
)

T = TypeVar("T")

class ResponseSingle(SQLModel, Generic[T]):
    data: T
    message: str
    success: bool

class ResponseMultiple(SQLModel, Generic[T]):
    data: List[T]
    message: str
    success: bool

@ingredients_router.post('/', response_model=ResponseSingle[Ingredient])
def create_ingredent(conn : DATABASE, ingredient: IngredientCreate):
    """
    Create a new ingredient
    """
    try:
        quantity = ingredient.quantity
        unit = ingredient.unit
        name = ingredient.name
        new_ing = Ingredient(name=name, quantity=quantity, unit=unit)
        conn.add(new_ing)
        conn.commit()
        conn.refresh(new_ing)
        resp = ResponseSingle[Ingredient](data=new_ing, message="Ingredient created successfully", success=True)
        return resp
    except Exception as e:
        conn.rollback()
        return {"message": "An error occurred"}


@ingredients_router.get('/', response_model=ResponseMultiple[Ingredient])
def get_all_ingredient():
  """
  Get all ingredients
  """
  return {"data": "all ingredients"}


@ingredients_router.get("/{id}", response_model=ResponseSingle[Ingredient])
def get_ingredient():
  """
    get a particular ingredient
  """
  
  return {"data": "A single ingredient"}

@ingredients_router.patch("/{id}", response_model=ResponseSingle[Ingredient])
def update_ingredient():
  
  return {"data" : "update....."}


@ingredients_router.delete("/{id}", response_model=ResponseSingle[Ingredient])
def delete_ingredient():
  """
  Delete a particular ingredient
  """
  return {"data": "delete ingredient"}