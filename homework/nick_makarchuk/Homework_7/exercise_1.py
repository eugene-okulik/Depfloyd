number = 1234
user_number = 0

while number != user_number:
    user_number = int(input('Введите цифру: '))
    if number != user_number:
        print(f'попробуйте снова')
    else:
        print(f'Поздравляю! Вы угадали!')
