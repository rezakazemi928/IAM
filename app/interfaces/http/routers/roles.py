from fastapi import APIRouter, Path

router = APIRouter(prefix="/roles")

@router.get("/{name}", status_code=200)
async def get_roles_by_name(name:str = Path(..., description="role name")):
    pass