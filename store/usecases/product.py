from store.database.mongo import db_client
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from tests.schemas.product import ProductIn


class ProductUseCase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn):
        self.collection.insert_one(body.model_dump())


product_usecase = ProductUseCase()
