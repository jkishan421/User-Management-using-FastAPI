import pytest
from httpx import AsyncClient

BASE_URL = "http://localhost:8080"


@pytest.mark.asyncio
async def test_delete_user_by_id():
    user_id = "4776a195-9cb0-4f08-9ce8-2a58f692addc"

    async with AsyncClient(base_url=BASE_URL) as client:
        # Test deleting a user with a valid ID
        response = await client.delete(f"/user/{user_id}")
        assert response.status_code == 204

        # Test deleting a user with an invalid ID
        invalid_user_id = "invalid_id"
        response = await client.delete(f"/user/{invalid_user_id}")
        assert response.status_code == 404
