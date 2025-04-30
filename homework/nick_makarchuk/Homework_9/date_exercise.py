import datetime

exercise_date = "Jan 15, 2023 - 12:05:33"

new_date = datetime.datetime.strptime(exercise_date, "%b %d, %Y - %H:%M:%S")

full_mouth_name = new_date.strftime("%B")
human_date = new_date.strftime('%d.%m.%Y, %H:%M')
print(full_mouth_name)
print(human_date)
