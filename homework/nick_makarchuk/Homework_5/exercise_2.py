ops_result_1 = 'результат операции: 42'
ops_result_2 = 'результат операции: 514'
ops_result_3 = 'результат работы программы: 9'

idx_1 = ops_result_1.index(':')
num_1 = int(ops_result_1[idx_1 + 1:].strip())

idx_2 = ops_result_2.index(':')
num_2 = int(ops_result_2[idx_2 + 1:].strip())

idx_3 = ops_result_3.index(':')
num_3 = int(ops_result_3[idx_3 + 1:].strip())

print(num_1 + 10)
print(num_2 + 10)
print(num_3 + 10)
