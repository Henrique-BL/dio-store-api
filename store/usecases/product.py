from typing import List
from uuid import UUID

import pymongo
from store.core.exceptions import NotFoundException
from store.database.mongo import db_client
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from tests.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut


class ProductUseCase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductOut(**body.model_dump())

        await self.collection.insert_one(product.model_dump())

        return product

    async def get(self, id: UUID) -> ProductOut:
        product = await self.collection.find_one({"id": id})

        if not product:
            raise NotFoundException(f"Product not found with id {id}")

        return ProductOut(**product)

    async def query(self) -> List[ProductOut]:
        return [ProductOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_dump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return ProductUpdateOut(**result)


product_usecase = ProductUseCase()
