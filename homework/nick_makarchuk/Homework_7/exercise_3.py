def extract_and_add_ten(text):
    num = int(text.split(':', 1)[1].strip())
    return num + 10


ops_result_1 = 'результат операции: 42'
ops_result_2 = 'результат операции: 54'
ops_result_3 = 'результат работы программы: 209'
ops_result_4 = 'результат: 9'


print(extract_and_add_ten(ops_result_1))
print(extract_and_add_ten(ops_result_2))
print(extract_and_add_ten(ops_result_3))
print(extract_and_add_ten(ops_result_4))
