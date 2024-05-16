import pytest
import requests

BASE_URL = "http://localhost:8080"


# Test case: Get user by ID
def test_get_file_path():
    user_id = "4776a195-9cb0-4f08-9ce8-2a58f692addc"  # Replace "user_id" with the ID of an existing user
    response = requests.get(f"{BASE_URL}/user/{user_id}/file-paths/")
    assert response.status_code == 200

    # Test getting a user by ID with an invalid ID
    invalid_user_id = "123"
    response = requests.get(f"{BASE_URL}/user/{invalid_user_id}")
    assert response.status_code == 404
