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
                    print(f"Попытка {i+1}/{attempts} не удалась: {e}")
                    if i == attempts - 1:
                        raise
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

# Пример использования
@retry(attempts=5, delay=1)
def unstable_network_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Сеть недоступна")
    return "Данные получены"

print(unstable_network_call())