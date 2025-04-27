import sys


sys.set_int_max_str_digits(100_000)

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci_generator()
targets = {5, 200, 1000, 100000}

for idx, num in enumerate(gen, start=1):
    if idx in targets:
        print(f"{idx}-е число Фибоначчи: {num}")
        targets.remove(idx)
        if not targets:
            break
