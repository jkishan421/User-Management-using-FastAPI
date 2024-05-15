import pytest
import requests

BASE_URL = "http://localhost:8080"


def test_update_user_by_id():
    user_id = "bf048cde-14e7-4011-a0e7-306ee4cba59f"  # Replace "123" with the ID of an existing user

    # Test updating a user with valid data
    updated_data = {"username": "updated_username", "email": "updated_email@example.com"}
    response = requests.put(
        f"{BASE_URL}/user/{user_id}",
        json=updated_data
    )
    assert response.status_code == 200

    # Test updating a user with invalid data
    invalid_data = {"username": "", "email": "invalid_email"}
    response = requests.put(
        f"{BASE_URL}/user/{user_id}",
        json=invalid_data
    )
    assert response.status_code == 422

    # Test updating a user with a non-existing ID
    non_existing_user_id = "non_existing_id"
    response = requests.put(
        f"{BASE_URL}/user/{non_existing_user_id}",
        json=updated_data
    )
    assert response.status_code == 404
