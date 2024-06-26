from uuid import UUID
from store.database.mongo import db_client
import asyncio
import pytest

from tests.factories import product_data, products_data
from store.schemas.product import ProductIn, ProductUpdate
from store.usecases.product import product_usecase
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()

    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collections_names = await mongo_client.get_database().list_collection_names()
    for name in collections_names:
        if name.startswith("system"):
            continue

    await mongo_client.get_database()[name].delete_many({})


@pytest.fixture
def product_id() -> UUID:
    return UUID("a1ff7af1-4868-437e-ae4b-9c4f6bb11a77")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def product_up(product_id):
    return ProductUpdate(**product_data(), id=product_id)


@pytest.fixture
async def product_inserted(product_in):
    return await product_usecase.create(body=product_in)


@pytest.fixture
def products_in():
    return [ProductIn(**product) for product in products_data()]


@pytest.fixture
async def products_inserted(products_in):
    return [await product_usecase.create(body=product) for product in products_in]


@pytest.fixture
async def client() -> AsyncClient:
    from store.main import app

    async with AsyncClient(app=app, base_url="http://store") as client:
        yield client


@pytest.fixture
def products_url() -> str:
    return "/products/"
