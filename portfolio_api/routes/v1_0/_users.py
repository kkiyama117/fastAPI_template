from typing import List

from fastapi import APIRouter, Depends, responses, status, HTTPException
from firebase_admin import auth

from portfolio_api import exceptions
from portfolio_api.domains.user import UserGet, UserCreate, UserUpdate
from portfolio_api.db.user import operations
from portfolio_api.middlewares import firebase_auth

router = APIRouter()


@router.get("/me/", response_model=UserGet)
async def get_own_user(current_user=Depends(firebase_auth.current_firebase_user)):
    user_auth = auth.get_user(current_user)
    return await operations.get_user_by_email(user_auth.email)


@router.get("/", response_model=List[UserGet])
async def get_users():
    return await operations.get_users()


@router.get("/{user_id}/", response_model=UserGet)
async def get_user(user_id: int):
    result = await operations.get_user(user_id)
    if result is not None:
        return result
    else:
        return responses.Response(status_code=status.HTTP_204_NO_CONTENT, content="")


@router.post("/", response_model=UserGet, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    try:
        return await operations.create_user(user_data)
    except exceptions.UserAlreadyExistException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except exceptions.DatabaseException as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/{user_id}/", response_model=UserGet)
async def update_user(user_id: int, user_data: UserUpdate):
    try:
        return await operations.update_user(user_id, user_data)
    except exceptions.BadRequestException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except exceptions.UserNotExistException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except exceptions.DatabaseException as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    try:
        return await operations.delete_user(user_id)
    except exceptions.UserNotExistException as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except exceptions.DatabaseException as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
