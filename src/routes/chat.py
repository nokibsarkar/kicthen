from fastapi import APIRouter
from ..database import *

chat_router = APIRouter(
    prefix="/chat",
    tags=["chat"],   
)

@chat_router.get('/', response_model=ResponseSingle[Recipe])
def chat(query: str, conn : DATABASE):
    """
    Query the Chatbot about the recipe
    :query str: The query to ask the chatbot like "I want to make a cake"
    """
    stmt = select(Ingredient)
    ingredients = conn.exec(stmt).all()
    print(ingredients)
    resp = ResponseSingle[Recipe](data=None, message="An error occurred", success=False)
    return {"data": query, "success": True}