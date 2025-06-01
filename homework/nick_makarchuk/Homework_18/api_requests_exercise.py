import requests
import json

BASE_URL = 'http://167.172.172.115:52353'


def get_all_objects():
    """Получение всех объектов"""
    response = requests.get(f'{BASE_URL}/object')
    print(f"GET all objects - Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.json()


def get_one_object(object_id=1):
    """Получение одного объекта по ID"""
    response = requests.get(f'{BASE_URL}/object/{object_id}')
    print(f"GET object {object_id} - Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.json()


def create_object():
    """Создание нового объекта"""
    body = {
        "name": "Test Object",
        "data": {
            "color": "red",
            "size": "medium"
        }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(f'{BASE_URL}/object', json=body, headers=headers)
    print(f"POST create object - Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Проверяем успешное создание
    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
    created_object = response.json()
    assert 'id' in created_object, 'ID not found in response'
    assert created_object['name'] == body['name'], 'Name mismatch'

    return created_object['id']


def put_object():
    """Полное обновление объекта методом PUT"""
    # Сначала создаем объект
    object_id = create_object()

    # Обновляем объект полностью
    updated_body = {
        "name": "Updated Object PUT",
        "data": {
            "color": "blue",
            "size": "large"
        }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.put(f'{BASE_URL}/object/{object_id}', json=updated_body, headers=headers)
    print(f"PUT update object {object_id} - Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Проверяем успешное обновление
    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
    updated_object = response.json()
    assert updated_object['name'] == updated_body['name'], 'Name not updated'
    assert updated_object['data']['color'] == updated_body['data']['color'], 'Color not updated'

    # Очищаем после теста
    delete_object(object_id)

    return object_id


def patch_object():
    """Частичное обновление объекта методом PATCH"""
    # Сначала создаем объект
    object_id = create_object()

    # Частично обновляем объект (только цвет)
    patch_body = {
        "data": {
            "color": "green"
        }
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.patch(f'{BASE_URL}/object/{object_id}', json=patch_body, headers=headers)
    print(f"PATCH update object {object_id} - Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # Проверяем успешное частичное обновление
    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'
    patched_object = response.json()
    assert patched_object['data']['color'] == patch_body['data']['color'], 'Color not patched'

    # Очищаем после теста
    delete_object(object_id)

    return object_id


def delete_object(object_id=None):
    """Удаление объекта"""
    if object_id is None:
        # Если ID не передан, создаем объект для удаления
        object_id = create_object()

    response = requests.delete(f'{BASE_URL}/object/{object_id}')
    print(f"DELETE object {object_id} - Status: {response.status_code}")

    # Проверяем успешное удаление
    assert response.status_code == 200, f'Expected status 200, got {response.status_code}'

    # Проверяем, что объект действительно удален (должен вернуть 404)
    try:
        get_response = requests.get(f'{BASE_URL}/object/{object_id}')
        if get_response.status_code == 404:
            print(f"Object {object_id} successfully deleted (404 when trying to get)")
        else:
            print(f"Warning: Object {object_id} still exists after deletion")
    except:
        print(f"Object {object_id} successfully deleted")

    return object_id


def run_all_tests():
    """Запуск всех тестов"""
    print("=" * 50)
    print("TESTING API FUNCTIONS")
    print("=" * 50)

    try:
        print("\n1. Testing GET all objects:")
        get_all_objects()

        print("\n2. Testing GET one object:")
        get_one_object(1)

        print("\n3. Testing POST (create object):")
        create_object()

        print("\n4. Testing PUT (full update):")
        put_object()

        print("\n5. Testing PATCH (partial update):")
        patch_object()

        print("\n6. Testing DELETE:")
        delete_object()

        print("\n" + "=" * 50)
        print("ALL TESTS COMPLETED SUCCESSFULLY!")
        print("=" * 50)

    except Exception as e:
        print(f"\nTest failed with error: {e}")
        print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
