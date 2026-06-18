from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

# Пример использования
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(40))  # Вычисляется быстро благодаря кэшу