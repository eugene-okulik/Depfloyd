from locust import task, HttpUser
import random
import string
import json


def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))


class ApiProject(HttpUser):

    def on_start(self):
        # Получаем список id существующих объектов при запуске пользователя
        response = self.client.get('/object')
        if response.ok:
            json_response = response.json()
            self.ids = [item["id"] for item in json_response.get("data", [])]
        else:
            self.ids = []
            print(f"Ошибка при получении данных объектов: {response.status_code}")

    @task(1)
    def get_all_objects(self):
        self.client.get('/object')

    @task(2)
    def get_one_object(self):
        if self.ids:
            selected_id = random.choice(self.ids)
            self.client.get(f'/object/{selected_id}')

    @task(2)
    def create_object(self):
        payload = {
            "name": random_string(),
            "data": {
                "color": random.choice(["white", "red", "green", "black", "silver"]),
                "size": random.choice(["small", "medium", "big"])
            }
        }
        response = self.client.post('/object', json=payload)
        if response.ok:
            new_obj = response.json()
            obj_id = new_obj.get("id")
            if obj_id:
                self.ids.append(obj_id)
        else:
            print(f"Ошибка при создании объекта: {response.status_code}")

    @task(1)
    def put_object(self):
        if self.ids:
            selected_id = random.choice(self.ids)
            payload = {
                "name": random_string(),
                "data": {
                    "color": random.choice(["white", "red", "green", "black", "silver"]),
                    "size": random.choice(["small", "medium", "big"])
                }
            }
            self.client.put(f'/object/{selected_id}', json=payload)

    @task(1)
    def patch_object(self):
        if self.ids:
            selected_id = random.choice(self.ids)
            # Изменяем либо name, либо data случайным образом
            if random.choice([True, False]):
                payload = {"name": random_string()}
            else:
                payload = {"data": {
                    "color": random.choice(["white", "red", "green", "black", "silver"]),
                    "size": random.choice(["small", "medium", "big"])
                }}
            self.client.patch(f'/object/{selected_id}', json=payload)

    @task(1)
    def delete_object(self):
        if self.ids:
            selected_id = random.choice(self.ids)
            response = self.client.delete(f'/object/{selected_id}')
            if response.status_code in (200, 204):
                self.ids.remove(selected_id)
