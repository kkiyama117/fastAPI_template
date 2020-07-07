from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def hello():
    return {"msg": "hello world!", "status": "ok"}
