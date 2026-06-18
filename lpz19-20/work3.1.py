import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️ {func.__name__}: {end - start:.6f} сек")
        return result
    return wrapper

def cache(func):
    cache_storage = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_storage:
            print(f"🔁 Кэш для {func.__name__}{args}")
            return cache_storage[key]
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result
    return wrapper

# Вариант 1: сначала @timer, потом @cache
@timer
@cache
def fib1(n):
    if n <= 1:
        return n
    return fib1(n-1) + fib1(n-2)

# Вариант 2: сначала @cache, потом @timer
@cache
@timer
def fib2(n):
    if n <= 1:
        return n
    return fib2(n-1) + fib2(n-2)

print("=== Порядок: @timer потом @cache ===")
print(fib1(30))
print(fib1(30))  # второй вызов – из кэша, время должно быть очень маленьким

print("\n=== Порядок: @cache потом @timer ===")
print(fib2(30))
print(fib2(30))