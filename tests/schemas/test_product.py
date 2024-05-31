from uuid import UUID

from pydantic import ValidationError
import pytest
from tests.factories import product_data
from tests.schemas.product import ProductIn


def test_schemas_sucess():
    data = product_data()

    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 Pro Max"
    assert isinstance(product.id, UUID)


def test_schemas_error():
    data = product_data()

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14 Pro Max", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }