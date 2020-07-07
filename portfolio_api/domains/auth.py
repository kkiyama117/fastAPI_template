from pydantic import BaseModel


class _Auth(BaseModel):
    id: int
    email: str
    is_active: bool = True
    is_admin: bool = False
