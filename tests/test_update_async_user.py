import pytest
from httpx import AsyncClient

BASE_URL = "http://localhost:8080"


@pytest.mark.asyncio
async def test_update_user_by_id():
    user_id = "8c2d25ef-f470-4084-8f4a-d4f53c858120"  # Replace with the ID of an existing user

    async with AsyncClient(base_url=BASE_URL) as client:
        # Test updating a user with valid data
        updated_data = {"username": "updated_username", "email": "updated_email@example.com"}
        response = await client.put(
            f"/user/{user_id}",
            json=updated_data
        )
        assert response.status_code == 200

        # Test updating a user with invalid data
        invalid_data = {"username": "", "email": "invalid_email"}
        response = await client.put(
            f"/user/{user_id}",
            json=invalid_data
        )
        assert response.status_code == 422

        # Test updating a user with a non-existing ID
        non_existing_user_id = "non_existing_id"
        response = await client.put(
            f"/user/{non_existing_user_id}",
            json=updated_data
        )
        assert response.status_code == 404
