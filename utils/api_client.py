import requests
from utils.config import BASE_URL, HEADERS

class APIClient:

    def __init__(self, base_url=BASE_URL, headers=HEADERS):
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint):
        """Send a GET request."""
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        return response

    def post(self, endpoint, data):
        """Send a POST request with data."""
        response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers=self.headers)
        return response

    def delete(self, endpoint):
        """Send a DELETE request."""
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self.headers)
        return response

    def put(self, endpoint, data):
        """Send a PUT request with data."""
        response = requests.put(f"{self.base_url}/{endpoint}", json=data, headers=self.headers)
        return response
