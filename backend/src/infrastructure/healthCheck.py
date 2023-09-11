from fastapi import APIRouter

router = APIRouter()


@router.get("/api/healthcheck")
async def healthcheck() -> bool:
    return True
