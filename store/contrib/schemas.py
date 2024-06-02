from pydantic import BaseModel


class OutMixin(BaseModel):
    class Config:
        from_attributes = True
