number = 1234
user_number = 0

while number != user_number:
    user_number = int(input('Введите цифру: '))
    if number != user_number:
        print('попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
