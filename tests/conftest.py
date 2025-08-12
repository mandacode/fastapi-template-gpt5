import asyncio
import pytest
import pytest_asyncio
from httpx import AsyncClient

from app.main import create_app


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def client():
    """Create an async test client."""
    app = create_app()
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client