from fastapi import APIRouter

router = APIRouter()


@router.get("/healthcheck")
async def healthcheck() -> bool:
    return True
