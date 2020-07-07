import sqlite3
from typing import List

from sqlalchemy import Table

from portfolio_api.domains import user
from portfolio_api import exceptions
from .schema import UserSchema
from .. import connection


async def get_users() -> List[user.UserGet]:
    users = UserSchema().get_table()
    query = users.select()
    return await connection.fetch_all(query)


async def get_user(user_id: int) -> user.UserGet:
    """Get User domain by id.

    Args:
        user_id (): id of user

    Returns:
        user.UserGet: user domain
    """
    users: Table = UserSchema().get_table()
    query = users.select().where(users.columns.id == user_id).limit(1)
    return await connection.fetch_one(query)


async def get_user_by_email(email: str) -> user.UserGet:
    """Get User domain by id.

    Args:
        email(str): email  of user

    Returns:
        user.UserGet: user domain
    """
    users: Table = UserSchema().get_table()
    query = users.select().where(users.columns.email == email).limit(1)
    return await connection.fetch_one(query)


async def create_user(user_data: user.UserCreate) -> user.UserGet:
    users: Table = UserSchema().get_table()
    query = users.insert().values(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        is_active=user_data.is_active,
        is_admin=False,
    )
    try:
        record_id = await connection.execute(query)
        return await get_user(record_id)
    except sqlite3.IntegrityError:
        raise exceptions.UserAlreadyExistException(f"{user_data.email} data is already exists")
    except Exception as e:
        raise exceptions.DatabaseException(str(e))


async def update_user(user_id: int, user_data: user.UserUpdate) -> user.UserGet:
    users: Table = UserSchema().get_table()
    query = (
        users.update()
        .where(users.columns.id == user_id)
        .values(
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            is_active=user_data.is_active,
            is_admin=False,
        )
    )
    try:
        result = await connection.execute(query)
        if not result:
            raise exceptions.UserNotExistException(f"user_{user_id} does not exist")
        return await get_user(user_id)
    except sqlite3.IntegrityError as e:
        raise exceptions.BadRequestException(str(e))


async def delete_user(user_id: int):
    users: Table = UserSchema().get_table()
    query = users.delete().where(users.columns.id == user_id)
    try:
        return await connection.execute(query)
    except sqlite3.IntegrityError:
        raise exceptions.UserNotExistException(f"user_{user_id} does not exist")
    except Exception as e:
        raise exceptions.DatabaseException(str(e))
