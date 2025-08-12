# FastAPI Template

A template repository for FastAPI projects with async SQLAlchemy and PostgreSQL.

## Features

- FastAPI application with proper project structure
- Async SQLAlchemy integration with PostgreSQL
- Docker and Docker Compose setup
- Testing setup with pytest
- Environment configuration with pydantic-settings

## Project Structure

```
src/app/
├── __init__.py
├── main.py                 # FastAPI application factory
├── database.py             # Async SQLAlchemy setup
├── api/
│   └── v1/
│       └── routes.py       # API routes
├── config/
│   └── settings.py         # Application settings
├── models/                 # SQLAlchemy models
├── repositories/           # Database repositories
├── schemas/                # Pydantic schemas
└── services/               # Business logic
tests/
├── __init__.py
├── conftest.py            # Test fixtures
└── test_api.py            # API tests
```

## Quick Start

### Using Docker Compose (Recommended)

1. Clone this repository
2. Copy environment variables:
   ```bash
   cp .env.example .env
   ```
3. Start the application:
   ```bash
   docker-compose up --build
   ```
4. Visit http://localhost:8000/docs for the API documentation

### Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up environment variables (copy from `.env.example`)
3. Start PostgreSQL database
4. Run the application:
   ```bash
   cd src
   uvicorn app.main:app --reload
   ```

## Testing

Run tests:
```bash
pytest
```

## API Endpoints

- `GET /api/v1/health` - Health check endpoint