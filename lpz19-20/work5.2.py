import time
from functools import wraps
from datetime import datetime

def log(filename="logs.txt"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            with open(filename, "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] {func.__name__}(")
                f.write(f"args={args}, kwargs={kwargs}) -> {result} ")
                f.write(f"время: {elapsed:.6f}с\n")
            return result
        return wrapper
    return decorator

# Пример использования
@log()
def add(a, b):
    return a + b

@log("mylog.txt")
def multiply(x, y):
    return x * y

add(3, 5)
multiply(4, 7)