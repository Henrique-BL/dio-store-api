from datetime import datetime, timezone
import uuid
from pydantic import UUID4, BaseModel, Field


def current_utc_time():
    return datetime.now(timezone.utc)


class OutMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=current_utc_time)
    updated_at: datetime = Field(default_factory=current_utc_time)
