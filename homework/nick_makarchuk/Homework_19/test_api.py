import pytest
import requests
import json

BASE_URL = 'http://167.172.172.115:52353'


@pytest.fixture(scope="session", autouse=True)
def session_setup_teardown():
    """Фикстура для выполнения действий до и после всех тестов"""
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture(autouse=True)
def test_setup_teardown():
    """Фикстура для выполнения действий до и после каждого теста"""
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture
def create_test_object():
    """Фикстура для создания объекта перед тестом и удаления после"""
    # Создаем объект для теста
    body = {
        "name": "Test Object for Test",
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(f'{BASE_URL}/object', json=body, headers=headers)
    assert response.status_code == 200, f'Failed to create test object: {response.status_code}'

    object_id = response.json()['id']
    print(f"\nCreated test object with id: {object_id}")

    yield object_id

    # Удаляем объект после теста
    try:
        delete_response = requests.delete(f'{BASE_URL}/object/{object_id}')
        if delete_response.status_code == 200:
            print(f"\nCleaned up test object with id: {object_id}")
    except Exception as e:
        print(f"\nWarning: Failed to cleanup object {object_id}: {e}")


@pytest.mark.critical
def test_get_all_objects():
    """Тест получения всех объектов"""
    response = requests.get(f'{BASE_URL}/object')

    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
    data = response.json()
    assert isinstance(data, dict), 'Response should be a dict'
    assert 'data' in data, 'Response should contain data field'
    assert isinstance(data['data'], list), 'Data field should contain a list'

    print(f"GET all objects - Status: {response.status_code}")
    print(f"Found {len(data['data'])} objects")


def test_get_one_object(create_test_object):
    """Тест получения одного объекта по ID"""
    object_id = create_test_object

    response = requests.get(f'{BASE_URL}/object/{object_id}')

    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
    data = response.json()
    assert 'id' in data, 'Response should contain id field'
    assert data['id'] == object_id, f'Expected id {object_id}, got {data.get("id")}'

    print(f"GET object {object_id} - Status: {response.status_code}")
    print(f"Response: {data}")


@pytest.mark.parametrize("test_data", [
    {
        "name": "Test Object 1",
        "data": {
            "color": "red",
            "size": "small"
        }
    },
    {
        "name": "Test Object 2",
        "data": {
            "color": "blue",
            "size": "medium"
        }
    },
    {
        "name": "Test Object 3",
        "data": {
            "color": "green",
            "size": "large"
        }
    }
])
def test_create_object(test_data):
    """Тест создания объекта с параметризацией"""
    headers = {'Content-Type': 'application/json'}

    response = requests.post(f'{BASE_URL}/object', json=test_data, headers=headers)

    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
    created_object = response.json()
    assert 'id' in created_object, 'ID not found in response'
    assert created_object['name'] == test_data['name'], 'Name mismatch'
    assert created_object['data']['color'] == test_data['data']['color'], 'Color mismatch'
    assert created_object['data']['size'] == test_data['data']['size'], 'Size mismatch'

    print(f"POST create object - Status: {response.status_code}")
    print(f"Created object: {created_object}")

    # Удаляем созданный объект для очистки
    object_id = created_object['id']
    try:
        requests.delete(f'{BASE_URL}/object/{object_id}')
    except Exception:
        pass  # Игнорируем ошибки удаления в этом тесте


@pytest.mark.medium
def test_put_object(create_test_object):
    """Тест полного обновления объекта методом PUT"""
    object_id = create_test_object

    updated_body = {
        "name": "Updated Object PUT",
        "data": {
            "color": "blue",
            "size": "large"
        }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(f'{BASE_URL}/object/{object_id}', json=updated_body, headers=headers)

    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
    updated_object = response.json()
    assert updated_object['name'] == updated_body['name'], 'Name not updated'
    assert updated_object['data']['color'] == updated_body['data']['color'], 'Color not updated'
    assert updated_object['data']['size'] == updated_body['data']['size'], 'Size not updated'

    print(f"PUT update object {object_id} - Status: {response.status_code}")
    print(f"Updated object: {updated_object}")


def test_patch_object(create_test_object):
    """Тест частичного обновления объекта методом PATCH"""
    object_id = create_test_object

    patch_body = {
        "data": {
            "color": "green"
        }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.patch(f'{BASE_URL}/object/{object_id}', json=patch_body, headers=headers)

    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
    patched_object = response.json()
    assert patched_object['data']['color'] == patch_body['data']['color'], 'Color not patched'

    print(f"PATCH update object {object_id} - Status: {response.status_code}")
    print(f"Patched object: {patched_object}")


def test_delete_object(create_test_object):
    """Тест удаления объекта"""
    object_id = create_test_object

    response = requests.delete(f'{BASE_URL}/object/{object_id}')

    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'

    # Проверяем, что объект действительно удален (должен вернуть 404)
    get_response = requests.get(f'{BASE_URL}/object/{object_id}')
    assert get_response.status_code == 404, f'Object should be deleted, but got status {get_response.status_code}'

    print(f"DELETE object {object_id} - Status: {response.status_code}")
    print(f"Object {object_id} successfully deleted (404 when trying to get)")


if __name__ == "__main__":
    # Запуск тестов с подробным выводом
    pytest.main([__file__, "-v", "-s"])
