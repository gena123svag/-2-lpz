import time
from functools import wraps

def retry(attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Попытка {i+1} не удалась: {e}")
                    if i == attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

# Пример:
@retry(attempts=5, delay=0.5)
def unstable_request():
    import random
    if random.random() < 0.8:
        raise ConnectionError("Ошибка сети")
    return "Успех!"

print(unstable_request())


"Где пригодится: при запросах к нестабильному API, чтении временно недоступного файла и т.п"