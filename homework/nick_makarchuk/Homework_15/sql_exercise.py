import mysql.connector as mysql

# Подключение к БД
conn = mysql.connect(
    user='',
    host='',
    passwd='',
    port='',
    database=''
)
cursor = conn.cursor()

# 1. Создаём группу
cursor.execute("""
    INSERT INTO `groups` (title, start_date, end_date)
    VALUES (%s, %s, %s)
""", ('Группа Б', '2024-09-01', '2025-06-01'))
cursor.execute("SELECT LAST_INSERT_ID()")
group_id = cursor.fetchone()[0]

# 2. Создаём студента и назначаем в группу
cursor.execute("""
    INSERT INTO students (name, second_name, group_id)
    VALUES (%s, %s, %s)
""", ('Nick', 'Makarchuk', group_id))
cursor.execute("SELECT LAST_INSERT_ID()")
student_id = cursor.fetchone()[0]

# 3. Добавляем книги и выдаём студенту
books = ['Война и мир', 'Преступление и наказание', 'Мастер и Маргарита']
cursor.executemany("""
    INSERT INTO books (title, taken_by_student_id)
    VALUES (%s, %s)
""", [(title, student_id) for title in books])

# 4. Добавляем предметы
subjects = ['Математика', 'История']
subject_ids = []
for title in subjects:
    cursor.execute("INSERT INTO subjets (title) VALUES (%s)", (title,))
    cursor.execute("SELECT LAST_INSERT_ID()")
    subject_ids.append(cursor.fetchone()[0])

# 5. Добавляем уроки (по 2 на каждый предмет)
lesson_ids = []
for i, subject_id in enumerate(subject_ids):
    for j in range(1, 3):
        lesson_title = f"Урок {j} по {subjects[i]}"
        cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)", (lesson_title, subject_id))
        cursor.execute("SELECT LAST_INSERT_ID()")
        lesson_ids.append(cursor.fetchone()[0])

# 6. Ставим оценки студенту за все уроки
marks = [(5 - i % 3, lesson_id, student_id) for i, lesson_id in enumerate(lesson_ids)]
cursor.executemany("""
    INSERT INTO marks (value, lesson_id, student_id)
    VALUES (%s, %s, %s)
""", marks)

# Подтверждаем всё одним коммитом
conn.commit()

# 7. Получаем и печатаем ВСЕ ДАННЫЕ о студенте одним запросом
query = """
SELECT
    s.id AS student_id,
    s.name,
    s.second_name,
    g.title AS group_title,
    b.title AS book_title,
    m.value AS mark,
    l.title AS lesson_title,
    subj.title AS subject_title
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets subj ON l.subject_id = subj.id
WHERE s.id = %s
"""
cursor.execute(query, (student_id,))
rows = cursor.fetchall()

print("\n📘 Информация о студенте:")
for row in rows:
    print(row)

# Завершаем
cursor.close()
conn.close()
