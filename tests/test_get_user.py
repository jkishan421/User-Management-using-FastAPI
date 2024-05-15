import pytest
import requests

BASE_URL = "http://localhost:8080"


def test_get_all_users():
    # Test getting all users when there are users in the database
    response = requests.get(f"{BASE_URL}/user/")
    assert response.status_code == 200


# Test case: Get user by ID
def test_get_user_by_id():
    user_id = "41ad5038-81e8-48d5-801f-74312e6c0df7"  # Replace "user_id" with the ID of an existing user
    response = requests.get(f"{BASE_URL}/user/{user_id}")
    assert response.status_code == 200

    # Test getting a user by ID with an invalid ID
    invalid_user_id = "123"
    response = requests.get(f"{BASE_URL}/user/{invalid_user_id}")
    assert response.status_code == 404
    # Assert that response indicates user not found or the expected structure of the response
