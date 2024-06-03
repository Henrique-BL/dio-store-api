from store.models.base import ProductBaseModel
from store.schemas.product import ProductIn


class ProductModel(ProductBaseModel, ProductIn):
    ...
