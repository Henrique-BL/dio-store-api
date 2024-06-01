from uuid import UUID
from store.database.mongo import db_client
import asyncio
import pytest

from tests.factories import product_data
from tests.schemas.product import ProductIn, ProductUpdate


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
    # await mongo_client.get_database()[name].delete_many({})


@pytest.fixture
def product_id() -> UUID:
    return UUID("a1ff7af1-4868-437e-ae4b-9c4f6bb11a77")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data(), id=product_id)


@pytest.fixture
def product_up():
    return ProductUpdate(**product_data(), id=product_id)
