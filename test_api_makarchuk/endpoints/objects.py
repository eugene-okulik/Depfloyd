import requests
from constants import BASE_URL


class ObjectsEndpoint:
    endpoint = f"{BASE_URL}/object"

    @classmethod
    def get_all(cls):
        return requests.get(cls.endpoint)

    @classmethod
    def get_one(cls, object_id):
        return requests.get(f"{cls.endpoint}/{object_id}")

    @classmethod
    def create(cls, name, color, size):
        payload = {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }
        return requests.post(cls.endpoint, json=payload)

    @classmethod
    def put(cls, object_id, name, color, size):
        payload = {
            "name": name,
            "data": {
                "color": color,
                "size": size
            }
        }
        return requests.put(f"{cls.endpoint}/{object_id}", json=payload)

    @classmethod
    def patch(cls, object_id, color=None, size=None):
        data = {}
        if color:
            data["color"] = color
        if size:
            data["size"] = size
        return requests.patch(f"{cls.endpoint}/{object_id}", json={"data": data})

    @classmethod
    def delete(cls, object_id):
        return requests.delete(f"{cls.endpoint}/{object_id}")
