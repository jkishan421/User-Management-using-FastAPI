import pytest
from httpx import AsyncClient

BASE_URL = "http://localhost:8080"


@pytest.mark.asyncio
async def test_get_file_path():
    user_id = "8c2d25ef-f470-4084-8f4a-d4f53c858120"  # Replace with the ID of an existing user

    async with AsyncClient(base_url=BASE_URL) as client:
        # Test getting file paths for a valid user ID
        response = await client.get(f"/user/{user_id}/file-paths/")
        assert response.status_code == 200
