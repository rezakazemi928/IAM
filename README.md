# IAM Service

Basic starter service using FastAPI with async SQLAlchemy.

## Requirements
- Python 3.10+
- PostgreSQL (or update `DATABASE_URL`)

## Setup
1. Create and activate a virtual environment.
2. Install dependencies (project-specific requirements file not included yet).
3. Create a `.env` file in the project root.

Example `.env`:
```env
APP_NAME=iam-service
ENV=dev
DATABASE_URL=postgresql+asyncpg://postgres:mypass@localhost:5435/iam_service
JWT_ISSUER=iam-service
JWT_AUDIENCE=food-delivery
JWT_SECRET=changeme
JWT_ACCESS_TTL_MIN=15
JWT_REFRESH_TTL_MIN=20160
```

## Run
From the project root:
```bash
uvicorn app.main:app --reload
```

## Project Structure
- `app/` FastAPI application code
- `app/core/` configuration
- `app/infrastructure/` database setup
- `app/interfaces/` HTTP routers

## Notes
- If you see `ModuleNotFoundError: No module named 'infrastructure'`, use absolute imports like `from app.infrastructure...` or run with `python -m app.main`.
