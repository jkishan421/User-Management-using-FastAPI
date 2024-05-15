import pytest
import requests

# Define the base URL of your FastAPI application
BASE_URL = "http://localhost:8080"


# Test case: Create User
def test_create_user():
    # Test creating a new user with valid username and email
    response = requests.post(
        f"{BASE_URL}/user/",
        json={"username": "test_user", "email": "test@example.com"}
    )
    assert response.status_code == 201

    # Test creating a new user with a username that already exists
    response = requests.post(
        f"{BASE_URL}/user/",
        json={"username": "test_user", "email": "test2@example.com"}
    )
    assert response.status_code == 409

    # Test creating a new user with an email that already exists
    response = requests.post(
        f"{BASE_URL}/user/",
        json={"username": "test_user2", "email": "test@example.com"}
    )
    assert response.status_code == 409

    # Test creating a new user with invalid email format
    response = requests.post(
        f"{BASE_URL}/user/",
        json={"username": "test_user3", "email": "invalid_email"}
    )
    assert response.status_code == 422
