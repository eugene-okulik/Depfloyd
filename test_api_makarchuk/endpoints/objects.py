import requests
from constants import BASE_URL


class ObjectsEndpoint:
    def __init__(self):
        self.base_url = f"{BASE_URL}/object"
        self.last_response = None
        self.last_data = None

    def get_all(self):
        self.last_response = requests.get(self.base_url)
        self.last_data = self.last_response.json()
        return self

    def get_one(self, object_id):
        self.last_response = requests.get(f"{self.base_url}/{object_id}")
        if self.last_response.status_code == 200:
            self.last_data = self.last_response.json()
        else:
            self.last_data = None
        return self

    def create(self, name, color, size):
        body = {"name": name, "data": {"color": color, "size": size}}
        self.last_response = requests.post(self.base_url, json=body)
        self.last_data = self.last_response.json()
        return self

    def put(self, object_id, name, color, size):
        body = {"name": name, "data": {"color": color, "size": size}}
        self.last_response = requests.put(f"{self.base_url}/{object_id}", json=body)
        self.last_data = self.last_response.json()
        return self

    def patch(self, object_id, color=None, size=None):
        data = {}
        if color:
            data["color"] = color
        if size:
            data["size"] = size
        self.last_response = requests.patch(f"{self.base_url}/{object_id}", json={"data": data})
        self.last_data = self.last_response.json()
        return self

    def delete(self, object_id):
        self.last_response = requests.delete(f"{self.base_url}/{object_id}")
        self.last_data = None
        return self

    def check_status_code(self, code):
        assert self.last_response.status_code == code, (
            f"Expected {code}, got {self.last_response.status_code}"
        )

    def validate_object_list(self):
        assert "data" in self.last_data
        assert isinstance(self.last_data["data"], list)

    def validate_object(self, expected_name=None, expected_color=None, expected_size=None):
        obj = self.last_data
        if expected_name is not None:
            assert obj["name"] == expected_name
        if expected_color is not None:
            assert obj["data"]["color"] == expected_color
        if expected_size is not None:
            assert obj["data"]["size"] == expected_size

    def check_status_not_found(self):
        assert self.last_response.status_code == 404, (
            f"Expected 404, got {self.last_response.status_code}"
        )
