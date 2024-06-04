from fastapi import APIRouter
from store.controller.product import router as produtos

rotas = APIRouter()

rotas.include_router(produtos, prefix="/products")
