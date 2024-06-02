from typing import List
import uuid

import pytest
from store.core.exceptions import NotFoundException
from store.usecases.product import product_usecase
from store.schemas.product import ProductOut, ProductUpdateOut


async def test_usecases_insert_return_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_return_sucess(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_return_not_found():
    id = uuid.uuid4()
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id)

    assert err.value.message == f"Product not found with id {id}"


@pytest.mark.usefixtures("products_inserted")
async def test_usecases_query_return_sucess():
    result: list[ProductOut] = await product_usecase.query()
    assert isinstance(result, List)
    assert len(result) > 1


async def test_usecases_update_return_sucess(product_inserted, product_up):
    product_up.price = 77.500
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


async def test_usecases_delete_return_sucess(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_delete_return_not_found():
    id = uuid.uuid4()

    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id)

    assert err.value.message == f"Product not found with id {id}"
