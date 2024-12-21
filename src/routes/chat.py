from fastapi import APIRouter
from ..database import *
from ..utils import parse_recipe
import google.generativeai as genai
chat_router = APIRouter(
    prefix="/chat",
    tags=["chat"],   
)

@chat_router.get('/', response_model=ResponseSingle[Recipe])
def chat(query: str, conn : DATABASE):
    """
    Query the Chatbot about the recipe
    `query` str: The query to ask the chatbot like "I want to make a cake"
    """

    # Fetch all the available ingredients
    stmt = select(Ingredient).where(Ingredient.quantity > 0)
    ingredients = conn.exec(stmt).all()
    ingredient_set = set(map(lambda x : x.name, ingredients))
    

    # Now select the recipe that has all the ingredients in the ingredient_set (available ingredients)
    selected_recipies = []
    recipies = parse_recipe.parse_recipe_file("static/recipe.txt")
    for recipe in recipies:
        if all(ingredient in ingredient_set for ingredient in recipe["ingredients"]):
            ingredient_list = ', '.join(recipe["ingredients"])
            selected_recipies.append(
                f"{recipe['title']} : {ingredient_list}"
            )
    selected_recipies = '\n'.join(selected_recipies)
    if selected_recipies:
        PROMPT = f"""
You are a helpful assistant for suggesting recipes based on user's preferences.
User Preferences: 
- User input: {query}.
- Recipies user have: {selected_recipies}.
Given the user’s preferences and available recipes, recommend the most suitable recipe from the list.
"""
        genai.configure(api_key="AIzaSyB2w89aSQVBd789r-ABGUBfCnNzaweDsHg")
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(PROMPT)
        
        
        resp = ResponseSingle[Recipe](data=selected_recipies, message=PROMPT, success=True)
        return resp
    else:
        return ResponseSingle[Recipe](data=None, message="No recipe found with available ingredients", success=False)
    