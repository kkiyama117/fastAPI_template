from pydantic import BaseModel


class _User(BaseModel):
    email: str = None
    first_name: str = None
    last_name: str = None
    # auth_id: str
    is_active: bool = True
    is_admin: bool = False
    # is_superuser: bool = False


# Define Database model domains below
class UserGet(_User):
    id: int

    class Config:
        orm_mode = True


# Model for connection to database
class UserCreate(_User):
    pass


class UserUpdate(_User):
    pass
