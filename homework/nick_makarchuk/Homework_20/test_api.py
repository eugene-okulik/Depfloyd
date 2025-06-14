import pytest
import requests
import json
import allure

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
@allure.feature('Objects API')
@allure.story('Получение всех объектов')
@allure.title('Получение списка всех объектов')
@allure.severity(allure.severity_level.NORMAL)
def test_get_all_objects():
    """Тест получения всех объектов"""
    with allure.step("Отправка GET запроса ко всем объектам"):
        response = requests.get(f'{BASE_URL}/object')

    with allure.step("Проверка корректности ответа"):
        assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
        data = response.json()
        assert isinstance(data, dict), 'Response should be a dict'
        assert 'data' in data, 'Response should contain data field'
        assert isinstance(data['data'], list), 'Data field should contain a list'

    print(f"GET all objects - Status: {response.status_code}")
    print(f"Found {len(data['data'])} objects")


@allure.feature('Objects API')
@allure.story('Получение одного объекта')
@allure.title('Получение объекта по ID')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_one_object(create_test_object):
    """Тест получения одного объекта по ID"""
    object_id = create_test_object
    with allure.step(f"Получение объекта по ID{object_id}"):
        response = requests.get(f'{BASE_URL}/object/{object_id}')
        assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
        data = response.json()
        assert 'id' in data, 'Response should contain id field'
        assert data['id'] == object_id, f'Expected id {object_id}, got {data.get("id")}'

    print(f"GET object {object_id} - Status: {response.status_code}")
    print(f"Response: {data}")


@allure.feature('Objects API')
@allure.story('Создание объектов')
@allure.title('Создание объекта с параметризацией')
@allure.severity(allure.severity_level.BLOCKER)
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

    with allure.step("Создание нового объекта"):
        response = requests.post(f'{BASE_URL}/object', json=test_data, headers=headers)

    with allure.step("Проверка корректности созданного объекта"):
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


@allure.feature('Objects API')
@allure.story('Обновление объектов')
@allure.title('Полное обновление объекта методом PUT')
@allure.severity(allure.severity_level.CRITICAL)
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

    with allure.step(f"Обновление объекта ID {object_id} методом PUT"):
        response = requests.put(f'{BASE_URL}/object/{object_id}', json=updated_body, headers=headers)
        assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
        updated_object = response.json()
        assert updated_object['name'] == updated_body['name'], 'Name not updated'
        assert updated_object['data']['color'] == updated_body['data']['color'], 'Color not updated'
        assert updated_object['data']['size'] == updated_body['data']['size'], 'Size not updated'

    print(f"PUT update object {object_id} - Status: {response.status_code}")
    print(f"Updated object: {updated_object}")


@allure.feature('Objects API')
@allure.story('Обновление объектов')
@allure.title('Частичное обновление объекта методом PATCH')
@allure.severity(allure.severity_level.NORMAL)
def test_patch_object(create_test_object):
    """Тест частичного обновления объекта методом PATCH"""
    object_id = create_test_object

    patch_body = {
        "data": {
            "color": "green"
        }
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step(f"Частичное обновление объекта ID {object_id} методом PATCH"):
        response = requests.patch(f'{BASE_URL}/object/{object_id}', json=patch_body, headers=headers)
        assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
        patched_object = response.json()
        assert patched_object['data']['color'] == patch_body['data']['color'], 'Color not patched'

    print(f"PATCH update object {object_id} - Status: {response.status_code}")
    print(f"Patched object: {patched_object}")


@allure.feature('Objects API')
@allure.story('Удаление объектов')
@allure.title('Удаление объекта')
@allure.severity(allure.severity_level.CRITICAL)
def test_delete_object(create_test_object):
    """Тест удаления объекта"""
    object_id = create_test_object
    with allure.step(f"Удаление объекта ID {object_id}"):
        response = requests.delete(f'{BASE_URL}/object/{object_id}')
        assert response.status_code == 200, f'Expected status 200, got {response.status_code}'

    with allure.step("Проверка, что объект удален"):
        get_response = requests.get(f'{BASE_URL}/object/{object_id}')
        assert get_response.status_code == 404, f'Object should be deleted, but got status {get_response.status_code}'

    print(f"DELETE object {object_id} - Status: {response.status_code}")
    print(f"Object {object_id} successfully deleted (404 when trying to get)")
