temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 
    32, 34, 30, 29, 25, 27, 22, 22, 23, 
    25, 29, 29, 31, 33, 31, 30, 32, 30, 
    28, 24, 23
    ]

def is_hot(temp):
    return temp > 28


new_temperatures = list(filter(is_hot, temperatures))
avg_temp = sum(new_temperatures) / len(new_temperatures)
print(new_temperatures)
print(max(new_temperatures))
print(min(new_temperatures))
print(round(avg_temp, 2))
