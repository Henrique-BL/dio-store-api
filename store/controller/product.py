from typing import List
from uuid import UUID
from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi import status
from fastapi import Path
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
from store.usecases.product import ProductUseCase

router = APIRouter(tags=["products"])


@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(
    body: ProductIn = Body(...), usecase: ProductUseCase = Depends()
) -> ProductOut:
    return await usecase.create(body=body)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(usecase: ProductUseCase = Depends()) -> List[ProductOut]:
    return await usecase.query()


@router.get(path="/{id}", status_code=status.HTTP_200_OK)
async def get(
    id: UUID = Path(alias="id"), usecase: ProductUseCase = Depends()
) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)


@router.patch(path="/{id}", status_code=status.HTTP_202_ACCEPTED)
async def patch(
    id: UUID = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUseCase = Depends(),
) -> ProductUpdateOut:
    try:
        return await usecase.update(id=id, body=body)
    except NotFoundException as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID = Path(alias="id"), usecase: ProductUseCase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)
