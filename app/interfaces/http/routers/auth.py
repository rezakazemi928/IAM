from fastapi import APIRouter, Depends
from app.application.usecases.register import RegisterUseCase, RegisterCommand
from app.interfaces.http.dependecies import get_register_use_case
from app.interfaces.http.schemas.auth import RegisterClientRequest, RegisterResponse


router = APIRouter()

@router.post("/register", response_model=RegisterResponse, status_code=201)
async def register(payload: RegisterClientRequest, use_case: RegisterUseCase = Depends(get_register_use_case)):
    cmd = RegisterCommand(**payload.model_dump())
    return await use_case.register_user(cmd)
    
