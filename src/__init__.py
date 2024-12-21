from fastapi import FastAPI


from .routes import ingredients_router

app = FastAPI()

app.include_router(ingredients_router)