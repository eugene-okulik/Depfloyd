import allure
from constants import (
    DEFAULT_NAME, DEFAULT_COLOR, DEFAULT_SIZE,
    UPDATED_NAME, UPDATED_COLOR, UPDATED_SIZE,
    PATCHED_COLOR, DELETE_NAME, DELETE_COLOR, DELETE_SIZE
)


@allure.feature('Objects API')
def test_create_object(endpoint):
    endpoint.create(DEFAULT_NAME, DEFAULT_COLOR, DEFAULT_SIZE)
    endpoint.check_status_code(200)
    endpoint.validate_object(expected_name=DEFAULT_NAME, expected_color=DEFAULT_COLOR, expected_size=DEFAULT_SIZE)
    endpoint.delete(endpoint.last_data["id"])


@allure.feature('Objects API')
def test_get_all_objects(endpoint):
    endpoint.get_all()
    endpoint.check_status_code(200)
    endpoint.validate_object_list()


@allure.feature('Objects API')
def test_get_one_object(endpoint, temp_object):
    endpoint.get_one(temp_object)
    endpoint.check_status_code(200)


@allure.feature('Objects API')
def test_put_object(endpoint, temp_object):
    endpoint.put(temp_object, UPDATED_NAME, UPDATED_COLOR, UPDATED_SIZE)
    endpoint.check_status_code(200)
    endpoint.validate_object(expected_name=UPDATED_NAME, expected_color=UPDATED_COLOR, expected_size=UPDATED_SIZE)


@allure.feature('Objects API')
def test_patch_object(endpoint, temp_object):
    original_object = endpoint.get_one(temp_object)
    original_name = original_object.last_data["name"]
    original_size = original_object.last_data["data"]["size"]
    endpoint.patch(temp_object, color=PATCHED_COLOR)
    endpoint.check_status_code(200)
    endpoint.validate_object(expected_color=PATCHED_COLOR)
    endpoint.get_one(temp_object)
    endpoint.check_status_code(200)
    endpoint.validate_object(expected_name=original_name,
                             expected_color=PATCHED_COLOR,
                             expected_size=original_size)


@allure.feature('Objects API')
def test_delete_object(endpoint, temp_object):
    endpoint.delete(temp_object)
    endpoint.check_status_code(200)
    endpoint.get_one(temp_object)
    endpoint.check_status_code(404)
