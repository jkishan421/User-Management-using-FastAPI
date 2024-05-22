import pytest
from httpx import AsyncClient

BASE_URL = "http://localhost:8080"


@pytest.mark.asyncio
async def test_get_all_users():
    async with AsyncClient(base_url=BASE_URL) as client:
        # Test getting all users when there are users in the database
        response = await client.get("/user/")
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_user_by_id():
    user_id = "4776a195-9cb0-4f08-9ce8-2a58f692addc"  # Replace with the ID of an existing user
    async with AsyncClient(base_url=BASE_URL) as client:
        response = await client.get(f"/user/{user_id}")
        assert response.status_code == 200

        invalid_user_id = "123"
        response = await client.get(f"/user/{invalid_user_id}")
        assert response.status_code == 404
