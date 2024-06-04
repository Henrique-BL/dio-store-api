from typing import List
import uuid
from httpx import AsyncClient
import pytest
from tests.factories import product_data
from fastapi import status


async def test_controller_post_return_sucess(client: AsyncClient, products_url: str):
    response = await client.post(products_url, json=product_data())
    content = response.json()

    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert content == {
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.usefixtures("products_inserted")
async def test_controller_query_return_sucess(client: AsyncClient, products_url: str):
    response = await client.get(products_url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1


async def test_controller_get_return_sucess(
    client: AsyncClient, products_url: str, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")
    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }
    assert response.status_code == status.HTTP_200_OK


async def test_controller_get_return_NotFound(client: AsyncClient, products_url: str):
    id = uuid.uuid4()
    response = await client.get(f"{products_url}{id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": f"Product not found with id {id}"}


async def test_controller_patch_return_sucess(
    client: AsyncClient, products_url: str, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"price": "10.000"}
    )
    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 Pro Max",
        "quantity": 10,
        "price": "10.000",
        "status": True,
    }

    assert response.status_code == status.HTTP_202_ACCEPTED


async def test_controller_delete_return_NO_CONTENT(
    client: AsyncClient, products_url: str, product_inserted
):
    response = await client.delete(url=f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_return_NOT_FOUND(
    client: AsyncClient, products_url: str, product_id
):
    response = await client.delete(url=f"{products_url}{product_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
