import os
from datetime import datetime, timedelta


# Путь к файлу
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, '..', '..', 'eugene_okulik', 'hw_13', 'data.txt')
file_path = os.path.normpath(file_path)

# Чтение и обработка файла
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        try:
            _, rest = line.split('. ', 1)
            date_str, action = rest.split(' - ', 1)
            dt = datetime.fromisoformat(date_str)


            if 'на неделю позже' in action:
                result = dt + timedelta(weeks=1)
                print(f"{date_str} -> через неделю: {result}")
            elif 'день недели' in action:
                result = dt.strftime('%A')
                print(f"{date_str} -> день недели: {result}")
            elif 'сколько дней назад' in action:
                today = datetime.now()
                delta = today - dt
                print(f"{date_str} -> дней назад {delta.days}")
            else:
                print(f"{date_str} -> неизвестное действие: {action}")
        except Exception as e:
            print(f"Ошибка обработки строки: {line}")
            print(e)
