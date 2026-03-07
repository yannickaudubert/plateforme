from fastapi import APIRouter, Depends

from app.dependencies import get_status_service
from app.models.system import SystemStatusResponse
from app.services.status_service import StatusService

router = APIRouter(prefix="/api/v1/system", tags=["system"])


@router.get("/status", response_model=SystemStatusResponse)
def system_status(status_service: StatusService = Depends(get_status_service)) -> SystemStatusResponse:
    return status_service.system_status()
