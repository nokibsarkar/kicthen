from fastapi import FastAPI


from .routes import ingredients_router
from .database import init_db
class KitchenManager(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_router(ingredients_router)
        init_db()
app = KitchenManager()