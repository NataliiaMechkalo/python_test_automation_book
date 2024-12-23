import pytest
from jsonschema import validate
from unittest.mock import Mock
import requests

# Fixture for base URL
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

# Fixture for headers
@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_auth_token"
    }

# Fixture for post payload
@pytest.fixture
def post_payload():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

# Helper function to create a mock response
def mock_response(status_code=200, json_data=None):
    mock_resp = Mock()
    mock_resp.status_code = status_code
    mock_resp.json = Mock(return_value=json_data)
    return mock_resp

# Test for fetching a post
def test_fetch_post(base_url, headers, mocker):
    mock_data = {"userId": 1, "id": 1, "title": "sample title", "body": "sample body"}
    mocker.patch('requests.get', return_value=mock_response(json_data=mock_data))

    response = requests.get(f"{base_url}/posts/1", headers=headers)
    assert response.status_code == 200
    assert response.json() == mock_data

# Test for creating a post
def test_create_post(base_url, headers, post_payload, mocker):
    mocker.patch('requests.post', return_value=mock_response(status_code=201, json_data={"id": 101, **post_payload}))

    response = requests.post(f"{base_url}/posts", json=post_payload, headers=headers)
    assert response.status_code == 201
    assert response.json() == {"id": 101, **post_payload}

# Test for updating a post
def test_update_post(base_url, headers, post_payload, mocker):
    updated_payload = {**post_payload, "title": "updated title"}
    mocker.patch('requests.put', return_value=mock_response(json_data={**updated_payload, "id": 1}))

    response = requests.put(f"{base_url}/posts/1", json=updated_payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == {**updated_payload, "id": 1}

# Test for deleting a post
def test_delete_post(base_url, headers, mocker):
    mocker.patch('requests.delete', return_value=mock_response(json_data={"status": "Post deleted"}))

    response = requests.delete(f"{base_url}/posts/1", headers=headers)
    assert response.status_code == 200
    assert response.json() == {"status": "Post deleted"}

# Parameterized test for fetching multiple posts
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_fetch_multiple_posts(base_url, headers, post_id, mocker):
    mocker.patch('requests.get', return_value=mock_response(json_data={"id": post_id}))
    response = requests.get(f"{base_url}/posts/{post_id}", headers=headers)
    assert response.json()["id"] == post_id

# Test using JSON Schema
def test_post_schema(base_url, headers, mocker):
    post_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }

    mocker.patch('requests.get', return_value=mock_response(json_data={
        "userId": 1, "id": 1, "title": "foo", "body": "bar"
    }))
    response = requests.get(f"{base_url}/posts/1", headers=headers)
    validate(instance=response.json(), schema=post_schema)