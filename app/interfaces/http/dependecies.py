from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.db.session import get_db_session
from app.infrastructure.db.repositories.account_repo_impl import SqlAlchemyAccountRepository
from app.infrastructure.otp_provider import PyOtpProvider
from app.application.usecases.register import RegisterUseCase

def get_account_repo(session: AsyncSession = Depends(get_db_session)):
    return SqlAlchemyAccountRepository(session)

def get_otp_provider() -> PyOtpProvider:
    return PyOtpProvider()

def get_register_use_case(
    repo=Depends(get_account_repo),
    otp_provider=Depends(get_otp_provider),
) -> RegisterUseCase:
    return RegisterUseCase(accounts=repo, otp_provider=otp_provider)
