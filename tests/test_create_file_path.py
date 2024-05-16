import pytest
import requests

# Define the base URL of your FastAPI application
BASE_URL = "http://localhost:8080"


# Test case: Create User
def test_create_file_path():
    # Test creating a new file_path with valid username and email
    user_id = "4776a195-9cb0-4f08-9ce8-2a58f692addc"  # Replace "user_id" with the ID of an existing user
    response = requests.post(
        f"{BASE_URL}/user/{user_id}/file-paths",
        json={"path": "sample_file_path123"}
    )
    assert response.status_code == 201

    # Test creating a new file with a path that already exists
    response = requests.post(
        f"{BASE_URL}/user/{user_id}/file-paths",
        json={"path": "sample_file_path123"}
    )
    assert response.status_code == 409
