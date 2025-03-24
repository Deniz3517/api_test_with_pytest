import pytest
import json
from utils.api_client import APIClient


# Fixture to initialize the API client
@pytest.fixture(scope="session")
def client():
    """Provides an instance of the API client."""
    return APIClient()


# Fixture to load test data for POST requests
@pytest.fixture
def post_test_data():
    """Loads test data for POST requests."""
    with open("/utils/test_data_json/post_test_data.json") as f:
        data = json.load(f)
    return data


@pytest.fixture
def put_test_data():
    """Loads test data for PUT requests"""
    with open("/utils/test_data_json/put_test_data.json", "r") as file:
        data = json.load(file)
    return data
