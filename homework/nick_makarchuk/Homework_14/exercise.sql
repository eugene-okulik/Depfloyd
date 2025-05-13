INSERT INTO students (name, second_name, group_id)
VALUES ('Nick', 'Makarchuk', NULL);

INSERT INTO books (title, taken_by_student_id)
VALUES
  ('Война и мир', 20332),
  ('Преступление и наказание', 20332),
  ('Мастер и Маргарита', 20332);

INSERT INTO `groups` (title, start_date, end_date)
VALUES ('Группа A', '2024-09-01', '2025-06-01');

UPDATE students SET group_id = 5056 WHERE id = 20332;

INSERT INTO subjets (title)
VALUES
  ('Математика'),
  ('История');

INSERT INTO lessons (title, subject_id)
VALUES
  ('Урок 1 по математике', (SELECT id FROM subjets WHERE title = 'Математика' LIMIT 1)),
  ('Урок 2 по математике', (SELECT id FROM subjets WHERE title = 'Математика' LIMIT 1));

INSERT INTO lessons (title, subject_id)
VALUES
  ('Урок 1 по истории', (SELECT id FROM subjets WHERE title = 'История' LIMIT 1)),
  ('Урок 2 по истории', (SELECT id FROM subjets WHERE title = 'История' LIMIT 1));

INSERT INTO marks (value, lesson_id, student_id)
VALUES
  (5, (SELECT id FROM lessons WHERE title = 'Урок 1 по математике' LIMIT 1), 20332),
  (4, (SELECT id FROM lessons WHERE title = 'Урок 2 по математике' LIMIT 1), 20332),
  (5, (SELECT id FROM lessons WHERE title = 'Урок 1 по истории' LIMIT 1), 20332),
  (3, (SELECT id FROM lessons WHERE title = 'Урок 2 по истории' LIMIT 1), 20332);

SELECT value AS Оценка
FROM marks
WHERE student_id = 20332;

SELECT title AS Книга
FROM books
WHERE taken_by_student_id = 20332;

SELECT
    s.name AS Имя,
    s.second_name AS Фамилия,
    g.title AS Группа,
    b.title AS Книга,
    m.value AS Оценка,
    l.title AS Занятие,
    sub.title AS Предмет
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjets sub ON l.subject_id = sub.id
WHERE s.id = 20332;