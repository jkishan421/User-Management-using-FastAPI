import pytest
import requests

# Define the base URL of your FastAPI application
BASE_URL = "http://localhost:8080"


def test_delete_user_by_id():
    user_id = "bf048cde-14e7-4011-a0e7-306ee4cba59f"

    # Test deleting a user with a valid ID
    response = requests.delete(f"{BASE_URL}/user/{user_id}")
    assert response.status_code == 204

    # Test deleting a user with an invalid ID
    invalid_user_id = "invalid_id"
    response = requests.delete(f"{BASE_URL}/user/{invalid_user_id}")
    assert response.status_code == 404
