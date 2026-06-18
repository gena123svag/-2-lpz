import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start:.4f} сек")
        return result
    return wrapper

# ПРИМЕНЯЕМ декоратор
@timer
def test():
    time.sleep(1)
    return "Готово"

# ВЫЗЫВАЕМ функцию
test()