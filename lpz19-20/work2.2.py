import time
from collections import OrderedDict

# Универсальный кэш с ограничением размера и возможностью очистки
def cache_universal(maxsize=100):
    def decorator(func):
        cache = OrderedDict()
        def wrapper(*args, **kwargs):
            # Ключ: позиционные аргументы + отсортированные именованные
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                # Перемещаем в конец (чтобы при переполнении удалить самый старый)
                cache.move_to_end(key)
                print(f"🔁 Кэш: {func.__name__}{args} из памяти")
                return cache[key]
            print(f"💡 Первый вызов: {func.__name__}{args}")
            result = func(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                removed = cache.popitem(last=False)
                print(f"🗑️ Удалён старый ключ: {removed[0]}")
            return result
        # Добавляем метод очистки кэша
        def clear():
            cache.clear()
            print("🧹 Кэш очищен")
        wrapper.clear = clear
        return wrapper
    return decorator

# Примеры использования
@cache_universal(maxsize=3)  # маленький кэш для демонстрации
def power(a, b):
    print(f"   (вычисляю {a}^{b})")
    return a ** b

@cache_universal()
def rectangle_area(width, height):
    print(f"   (вычисляю площадь {width}x{height})")
    return width * height

# Проверка
print("=== power ===")
print(power(2, 10))
print(power(2, 10))   # из кэша
print(power(3, 4))
print(power(4, 5))
print(power(5, 6))    # здесь может вытесниться самый старый ключ
print()

print("=== rectangle_area ===")
print(rectangle_area(5, 3))
print(rectangle_area(5, 3))  # из кэша
print(rectangle_area(7, 2))
print(rectangle_area(5, 3))  # всё ещё в кэше, если не вытеснили
print()

# Очистка кэша
print("=== Очистка кэша power ===")
power.clear()
print(power(2, 10))   # снова первый вызов