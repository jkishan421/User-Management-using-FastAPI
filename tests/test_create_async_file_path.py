import pytest
from httpx import AsyncClient

# Define the base URL of your FastAPI application
BASE_URL = "http://localhost:8080"


# Test case: Create User
@pytest.mark.asyncio
async def test_create_file_path():
    user_id = "8c2d25ef-f470-4084-8f4a-d4f53c858120"  # Replace with the ID of an existing user

    async with AsyncClient(base_url=BASE_URL) as client:
        # Test creating a new file_path with valid path
        response = await client.post(
            f"/user/{user_id}/file-paths/",
            json={"path": "sample_file_path321"}
        )
        assert response.status_code == 201

        # Test creating a new file with a path that already exists
        response = await client.post(
            f"/user/{user_id}/file-paths/",
            json={"path": "sample_file_path321"}
        )
        assert response.status_code == 409
