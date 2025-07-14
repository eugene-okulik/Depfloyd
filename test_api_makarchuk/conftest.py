import pytest
from endpoints.objects import ObjectsEndpoint
from constants import DEFAULT_COLOR, DEFAULT_SIZE
from utils.helpers import random_string


@pytest.fixture
def endpoint():
    return ObjectsEndpoint()


@pytest.fixture
def temp_object(endpoint):
    """Создать объект и удалить после теста."""
    name = f"Temp_{random_string(5)}"
    color = DEFAULT_COLOR
    size = DEFAULT_SIZE
    endpoint.create(name, color, size).check_status_code(200)
    obj_id = endpoint.last_data["id"]
    yield obj_id
    endpoint.delete(obj_id)
