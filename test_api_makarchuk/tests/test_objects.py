import pytest
from endpoints.objects import ObjectsEndpoint
from utils.helpers import random_string
from utils.validators import validate_object, validate_object_list
import allure


@pytest.fixture
def test_object():
    # Создание объекта перед тестом
    name = f"Temp_{random_string(5)}"
    color = "red"
    size = "small"
    response = ObjectsEndpoint.create(name, color, size)
    assert response.status_code == 200
    obj_id = response.json()['id']
    yield obj_id
    # Очистка после теста
    ObjectsEndpoint.delete(obj_id)


@allure.feature('Objects API')
def test_get_all_objects():
    response = ObjectsEndpoint.get_all()
    assert response.status_code == 200
    validate_object_list(response.json())


@allure.feature('Objects API')
def test_create_object():
    name = f"Obj_{random_string(5)}"
    color = "blue"
    size = "large"
    response = ObjectsEndpoint.create(name, color, size)
    assert response.status_code == 200
    obj = response.json()
    validate_object(obj, expected_name=name, expected_color=color, expected_size=size)
    ObjectsEndpoint.delete(obj['id'])


@allure.feature('Objects API')
def test_get_one_object(test_object):
    response = ObjectsEndpoint.get_one(test_object)
    assert response.status_code == 200
    obj = response.json()
    validate_object(obj)


@allure.feature('Objects API')
def test_put_object(test_object):
    name = f"Updated_{random_string(5)}"
    color = "green"
    size = "medium"
    response = ObjectsEndpoint.put(test_object, name, color, size)
    assert response.status_code == 200
    obj = response.json()
    validate_object(obj, expected_name=name, expected_color=color, expected_size=size)


@allure.feature('Objects API')
def test_patch_object(test_object):
    color = "yellow"
    response = ObjectsEndpoint.patch(test_object, color=color)
    assert response.status_code == 200
    obj = response.json()
    validate_object(obj, expected_color=color)


@allure.feature('Objects API')
def test_delete_object():
    name = f"Del_{random_string(5)}"
    color = "pink"
    size = "small"
    response = ObjectsEndpoint.create(name, color, size)
    assert response.status_code == 200
    obj_id = response.json()['id']
    del_response = ObjectsEndpoint.delete(obj_id)
    assert del_response.status_code == 200
    get_response = ObjectsEndpoint.get_one(obj_id)
    assert get_response.status_code == 404
