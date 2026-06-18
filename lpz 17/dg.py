# Лабораторная работа 17: Функциональное программирование

from functools import reduce

# ====== Часть 1: Разминка — преврати в lambda ======

double = lambda x: x * 2
is_negative = lambda x: x < 0
add = lambda a, b: a + b
max3 = lambda a, b, c: max(a, b, c)
get_first = lambda arr: arr[0] if arr else None

# ====== Часть 2: map() — путешествие на фабрику ======

# 1
print(list(map(lambda x: x + 10, [1, 2, 3, 4, 5])))
# 2
print(list(map(lambda x: x ** 2, [3, 7, 2, 9, 4])))
# 3
print(list(map(lambda x: x.upper(), ["a", "b", "c"])))
# 4
print(list(map(lambda x: "Студент " + x, ["Иван", "Анна", "Петр"])))
# 5
print(list(map(lambda x: x / 2, [10, 20, 30, 40])))

# Творческое: на фабрике упаковывают детали в коробки по 5 штук.
# Нужно посчитать, сколько коробок нужно для каждой партии.
details = [23, 45, 12, 67, 34]
boxes = list(map(lambda x: (x + 4) // 5, details))
print("Коробок нужно:", boxes)

# ====== Часть 3: filter() — кастинг талантов ======

# 1
print(list(filter(lambda x: x % 5 == 0, [10, 15, 20, 25, 30])))
# 2
print(list(filter(lambda x: len(x) > 3, ["кот", "собака", "ёж", "слон"])))
# 3
print(list(filter(lambda x: x > 0, [-5, 3, -2, 0, 7, -1, 8])))
# 4
print(list(filter(lambda x: x.startswith("А"), ["Анна", "Борис", "Алексей", "Виктор"])))
# 5
print(list(filter(lambda x: x > 18, [21, 18, 25, 16, 19, 30])))

# Творческое: отбор спортсменов в команду — рост > 175 и возраст < 30
candidates = [
    ("Иван", 180, 25),
    ("Петр", 170, 22),
    ("Анна", 165, 28),
    ("Олег", 190, 31),
    ("Мария", 178, 20)
]
selected = list(filter(lambda x: x[1] > 175 and x[2] < 30, candidates))
print("Прошли в команду:", [x[0] for x in selected])

# ====== Часть 4: map + filter — командная работа ======

# 1
print(list(map(lambda x: x * 10, filter(lambda x: x % 2 == 0, [3, 8, 5, 12, 7, 15]))))
# 2
print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6, 7, 8, 9]))))
# 3
print(list(map(lambda x: x / 5, filter(lambda x: x % 5 == 0, [10, 25, 30, 45, 50, 65]))))
# 4
print(list(map(lambda x: "сладкий " + x, filter(lambda x: x[0] in "аеёиоуыэюя", ["яблоко", "груша", "арбуз", "дыня"]))))
# 5
print(list(map(lambda x: x - 50, filter(lambda x: x > 200, [100, 150, 200, 250, 300]))))

# Творческое: товары дешевле 1000, начислить скидку 10%
prices = [1200, 500, 800, 1500, 300, 950]
discounted = list(map(lambda x: round(x * 0.9, 2), filter(lambda x: x < 1000, prices)))
print("Цены со скидкой:", discounted)

# ====== Часть 5: reduce() — соковыжималка ======

# 1 — Произведение
# шаг 1: 2*3=6, шаг 2: 6*4=24, шаг 3: 24*5=120
print(reduce(lambda a, b: a * b, [2, 3, 4, 5]))

# 2 — Максимум
# 7>3 → 7, 7<9 → 9, 9>2 → 9
print(reduce(lambda a, b: a if a > b else b, [7, 3, 9, 2]))

# 3 — Сумма
# 10+20=30, 30+30=60, 60+40=100, 100+50=150
print(reduce(lambda a, b: a + b, [10, 20, 30, 40, 50]))

# 4 — Склейка строк
# "Я" + "люблю" = "Ялюблю", + "Python" = "ЯлюблюPython"
print(reduce(lambda a, b: a + b, ["Я", "люблю", "Python"]))

# 5 — НОД
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(reduce(gcd, [5, 10, 15, 20]))

# Дополнительно: факториал 5
print(reduce(lambda a, b: a * b, range(1, 6)))

# ====== Часть 6: Сравнение стилей ======

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Способ 1: цикл
s = 0
for x in nums:
    if x % 2 == 0:
        s += x ** 2
print("Цикл:", s)

# Способ 2: map + filter + reduce
res = reduce(lambda a, b: a + b, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
print("Map/filter/reduce:", res)

# Способ 3: генератор
res2 = sum(x ** 2 for x in nums if x % 2 == 0)
print("Генератор:", res2)

# ====== Часть 7: Творческий проект ======

# Программа: "Школьный журнал успеваемости"
# Отбирает учеников с баллом >= 4 (filter),
# добавляет бонус 0.5 балла отличникам (map),
# считает средний балл (reduce).

students = [("Иван", 3.5), ("Анна", 4.5), ("Петр", 5.0), ("Мария", 4.0), ("Олег", 3.0)]

good = list(filter(lambda s: s[1] >= 4, students))
print("Хорошисты:", good)

bonus = list(map(lambda s: (s[0], min(s[1] + 0.5, 5.0)), filter(lambda s: s[1] >= 4, students)))
print("С бонусом:", bonus)

avg = reduce(lambda a, b: a + b, map(lambda s: s[1], bonus)) / len(bonus) if bonus else 0
print("Средний балл:", round(avg, 2))