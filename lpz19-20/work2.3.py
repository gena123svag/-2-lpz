import time
from collections import OrderedDict

def cache_ttl(seconds, maxsize=100):
    """
    Декоратор кэширования с временем жизни и ограничением размера.
    seconds: время жизни в секундах
    maxsize: максимальное количество записей в кэше
    """
    def decorator(func):
        cache = OrderedDict()  # ключ -> (результат, время_создания)

        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()

            # Проверяем, есть ли в кэше и не устарел ли
            if key in cache:
                result, created = cache[key]
                if now - created < seconds:
                    # Всё свежо – перемещаем ключ в конец (используем как LRU)
                    cache.move_to_end(key)
                    print(f"🔁 Кэш (ещё свежий): {func.__name__}{args}")
                    return result
                else:
                    print(f"⏰ Кэш устарел: {func.__name__}{args}")
                    # удаляем устаревший ключ (он всё равно перезапишется)
                    del cache[key]

            # Вычисляем заново
            print(f"💡 Вычисляем: {func.__name__}{args}")
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            # Ограничиваем размер кэша
            if len(cache) > maxsize:
                oldest_key, _ = cache.popitem(last=False)
                print(f"🗑️ Удалён самый старый ключ: {oldest_key}")

            return result

        # Метод очистки кэша
        def clear():
            cache.clear()
            print("🧹 Кэш полностью очищен")

        wrapper.clear = clear
        return wrapper
    return decorator


# ========== ПРОВЕРКА ==========
print("=== Кэш с TTL 5 секунд, размер кэша 2 ===")

@cache_ttl(seconds=5, maxsize=2)
def get_time():
    return time.time()

# Первый вызов – вычисляем
print(get_time())
time.sleep(1)
# Второй вызов – должен вернуть из кэша
print(get_time())
time.sleep(3)   # теперь прошло 4 секунды с первого вызова – кэш ещё жив
print(get_time())
time.sleep(3)   # дополнительно 3 секунды, итого 7 секунд – кэш устарел
print(get_time())

print("\n=== Проверка ограничения размера кэша ===")

@cache_ttl(seconds=10, maxsize=2)
def square(x):
    print(f"  вычисляю квадрат {x}")
    return x * x

print(square(2))   # 4
print(square(3))   # 9
print(square(4))   # 16 – превысит maxsize, вытеснится 2
print(square(2))   # 2 вытеснен, вычислится заново
print(square(3))   # 3 вытеснен? зависит от порядка, но суть ясна

print("\n=== Очистка кэша ===")
@cache_ttl(seconds=10)
def nothing():
    return 42

print(nothing())
nothing.clear()
print(nothing())  # после очистки вычисляется заново