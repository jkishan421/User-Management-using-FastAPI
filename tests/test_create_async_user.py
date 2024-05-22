import pytest
from httpx import AsyncClient

BASE_URL = "http://localhost:8080"


@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(base_url=BASE_URL) as client:
        # Test creating a new user with valid username and email
        response = await client.post(
            "/user/",
            json={"username": "test_user", "email": "test@example.com"}
        )
        assert response.status_code == 201

        # Test creating a new user with a username that already exists
        response = await client.post(
            "/user/",
            json={"username": "test_user", "email": "test2@example.com"}
        )
        assert response.status_code == 409

        # Test creating a new user with an email that already exists
        response = await client.post(
            "/user/",
            json={"username": "test_user2", "email": "test@example.com"}
        )
        assert response.status_code == 409

        # Test creating a new user with invalid email format
        response = await client.post(
            "/user/",
            json={"username": "test_user3", "email": "invalid_email"}
        )
        assert response.status_code == 422
