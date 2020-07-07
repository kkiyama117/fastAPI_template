from fastapi import APIRouter
from ._root import router as root
from ._users import router as user

router = APIRouter()
router.include_router(root)
router.include_router(
    user, prefix="/users", tags=["users"],
)
