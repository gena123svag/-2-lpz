# Простой декоратор кэша для одного аргумента
def cache_simple(func):
    cache = {}
    def wrapper(arg):
        if arg in cache:
            print(f"🔁 Кэш: берём результат для {arg} из памяти")
            return cache[arg]
        print(f"💡 Первый вызов: вычисляем результат для {arg}")
        result = func(arg)
        cache[arg] = result
        return result
    return wrapper

# 1. Функция факториала (уже была в примере)
@cache_simple
def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 2. Рекурсивное число Фибоначчи (без кэша было бы медленно)
@cache_simple
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 3. Возведение в степень (фиксируем основание, чтобы был один аргумент – показатель)
@cache_simple
def power_of_two(exp):
    return 2 ** exp

# 4. Проверка, является ли число простым
@cache_simple
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Проверки
print("=== Факториал ===")
print(factorial(5))
print(factorial(5))
print(factorial(7))
print(factorial(5))
print()

print("=== Фибоначчи ===")
print(fibonacci(10))
print(fibonacci(10))
print(fibonacci(8))
print()

print("=== Степень двойки ===")
print(power_of_two(10))
print(power_of_two(10))
print(power_of_two(12))
print()

print("=== Простые числа ===")
print(is_prime(17))
print(is_prime(17))
print(is_prime(20))