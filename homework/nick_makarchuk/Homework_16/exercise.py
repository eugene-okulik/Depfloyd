import csv
import mysql.connector as mysql
import os
import dotenv

dotenv.load_dotenv()

# Путь к CSV
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, '..', '..', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

# Чтение CSV
with open(file_path, newline='', encoding='utf-8') as csv_file:
    file_data = csv.DictReader(csv_file)
    csv_data = [dict(row) for row in file_data]

# Подключение к БД
db = mysql.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    database=os.getenv('DB_NAME'),
    port=os.getenv('DB_PORT')
)
cursor = db.cursor(dictionary=True)

# SQL-запрос к БД
cursor.execute('''
SELECT
    s.name,
    s.second_name,
    g.title AS group_title,
    b.title AS book_title,
    sub.title AS subject_title,
    l.title AS lesson_title,
    m.value AS mark_value
FROM students s
JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON b.taken_by_student_id = s.id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets sub ON l.subject_id = sub.id;
''')

db_data = cursor.fetchall()

# Нормализация
def normalize(row):
    return {k.strip(): str(v).strip() for k, v in row.items()}

normalized_db = [normalize(row) for row in db_data]
normalized_csv = [normalize(row) for row in csv_data]

# Поиск строк, которых нет в БД
missing_rows = [row for row in normalized_csv if row not in normalized_db]

# Результат
if missing_rows:
    print("Строки из CSV, которых нет в базе данных:")
    for row in missing_rows:
        print(row)
else:
    print("Все строки из CSV есть в базе.")

# Закрытие соединения
cursor.close()
db.close()
