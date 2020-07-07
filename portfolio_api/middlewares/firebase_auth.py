import logging

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status
from firebase_admin import auth
from firebase_admin.tenant_mgt import TenantIdMismatchError


def current_firebase_user(cred: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    """

    Args:
        cred (HTTPAuthorizationCredentials): Bearer token

    Returns:
        str: user id of firebase auth

    """
    try:
        decoded_token = auth.verify_id_token(cred.credentials)
    except (ValueError, TenantIdMismatchError) as e:
        logging.getLogger(__package__).warning(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return decoded_token.get("user_id")
