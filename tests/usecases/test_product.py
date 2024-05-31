from store.usecases.product import product_usecase
from tests.conftest import product_in


async def test_usecases_return_sucess():
    result = await product_usecase.create(product_in)

    # assert isinstance(result,ProductOut)
    assert result is None
