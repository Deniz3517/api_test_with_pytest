import pytest


# Test1: GET - Validate activities retrieval
@pytest.mark.test1
@pytest.fixture
def get_activities(client):
    """Fetch activities from the API."""
    response = client.get("Activities")
    return response

@pytest.mark.test1
def test_get_activities_status_code(get_activities):
    """Verify that the GET request returns status 200."""
    assert get_activities.status_code == 200, f"Expected 200, but got {get_activities.status_code}"


@pytest.mark.test1
def test_get_activities_format(get_activities):
    """Verify that the response body is in JSON format and is a list."""
    data = get_activities.json()
    assert isinstance(data, list), "Response should be a list!"
    assert len(data) > 0, "The list should not be empty!"


@pytest.mark.test1
@pytest.mark.parametrize("field", ["id", "title", "dueDate", "completed"])
def test_get_activities_fields(get_activities, field):
    """Verify that each activity contains the necessary fields."""
    data = get_activities.json()
    for item in data:
        assert field in item, f"{field} is missing from an activity!"


# Test2: POST - Create a new activity
@pytest.mark.test2
def test_post_activity(client, post_test_data):
    """Create a new activity and verify its data."""
    response = client.post("Activities", post_test_data)
    assert response.status_code == 200, "POST request failed!"
    response_data = response.json()
    assert response_data["title"] == post_test_data["title"], "Title mismatch!"
    assert response_data["dueDate"] == post_test_data["dueDate"], "Due date mismatch!"
    assert response_data["completed"] == post_test_data["completed"], "Completed status mismatch!"


# Test: PUT - Update an existing activity
@pytest.mark.test3
def test_put_activity(client, put_test_data):
    """Update an existing activity and verify its data."""
    activity_id = put_test_data["id"]  # Example activity ID to update
    response = client.put(f"Activities/{activity_id}", put_test_data)

    # Verify that the response status code is 200 (Success)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

    # Verify that the returned data is correct
    response_data = response.json()
    assert response_data["id"] == put_test_data[
        "id"], f"Expected ID {put_test_data['id']}, but got {response_data['id']}"
    assert response_data["title"] == put_test_data[
        "title"], f"Title mismatch: expected {put_test_data['title']}, but got {response_data['title']}"
    assert response_data["dueDate"] == put_test_data[
        "dueDate"], f"Due date mismatch: expected {put_test_data['dueDate']}, but got {response_data['dueDate']}"
    assert response_data["completed"] == put_test_data[
        "completed"], f"Completed status mismatch: expected {put_test_data['completed']}, but got {response_data['completed']}"
