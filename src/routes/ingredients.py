from fastapi import APIRouter

ingredients_router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
    responses={404: {"description": "Not found"}},
)

@ingredients_router.post('/')
def create_ingredent():
    return {"message": "Create ingredient"}

