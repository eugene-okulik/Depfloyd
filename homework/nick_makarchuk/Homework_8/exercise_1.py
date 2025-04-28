import random


salary = int(input("Enter your salary: "))
original_salary = salary
bonus = random.choice([True, False])

if bonus:
    salary += random.randint(1000, 5000)

print(f'{original_salary}, {bonus} - ${salary}')
