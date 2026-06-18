import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__}: {end - start:.4f} сек")
        return result
    return wrapper

# 1. Функция, которая считает сумму чисел от 1 до 1 000 000
@timer
def sum_to_million():
    total = 0
    for i in range(1, 1_000_001):
        total += i
    return total

# 2. Функция, которая считает факториал числа 10
@timer
def fact_10():
    res = 1
    for i in range(2, 11):
        res *= i
    return res

# 3. Функция, которая создаёт список из 10 000 чисел и сортирует его
@timer
def sort_10000():
    data = list(range(10000, 0, -1))
    return sorted(data)

# Вызов всех функций (чтобы увидеть вывод времени)
sum_to_million()
fact_10()
sort_10000()