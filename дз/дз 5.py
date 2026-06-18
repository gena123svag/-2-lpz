import random
import copy

# =========================
# Задача 1: Практика со списками
# =========================
print("Задача 1: Практика со списками")

# 1) Список из 10 случайных чисел 1..100
lst = [random.randint(1, 100) for _ in range(10)]
print("Исходный список:", lst)

# 2) Три копии разными способами
copy1 = lst.copy()          # способ 1
copy2 = lst[:]              # способ 2
copy3 = list(lst)           # способ 3
print("Копия 1:", copy1)
print("Копия 2:", copy2)
print("Копия 3:", copy3)

# 3) Отсортировать одну по возрастанию, другую по убыванию
asc = sorted(copy1)                 # по возрастанию
desc = sorted(copy2, reverse=True)  # по убыванию
print("Сортировка ↑:", asc)
print("Сортировка ↓:", desc)

# 4) Удалить из исходного списка все четные числа
lst_no_even = [x for x in lst if x % 2 != 0]
print("Без четных:", lst_no_even)

# 5) Найти max и min (в исходном)
print("Минимум:", min(lst))
print("Максимум:", max(lst))


# =========================
# Задача 2: Генераторы списков
# =========================
print("Задача 2: Генераторы списков")

# 1) Квадраты 1..20
squares = [x * x for x in range(1, 21)]
print("Квадраты 1..20:", squares)

# 2) Числа 1..100, делятся на 3 и на 5 (то есть на 15)
div_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print("Делятся на 3 и 5:", div_3_and_5)

# 3) Из строки сделать список символов в верхнем регистре
text = "Python is awesome!"
upper_chars = [ch.upper() for ch in text]
print("Символы в верхнем регистре:", upper_chars)

# 4) Перевести температуры C -> F для [0, 20, 100, -10, 25]
celsius = [0, 20, 100, -10, 25]
fahrenheit = [c * 9 / 5 + 32 for c in celsius]
print("Цельсий:", celsius)
print("Фаренгейт:", fahrenheit)

# 5) Из ["apple","banana","cherry","date"] сделать список длин слов, но только для слов > 4 символов
words = ["apple", "banana", "cherry", "date"]
lengths_gt4 = [len(w) for w in words if len(w) > 4]
print("Длины слов (длина > 4):", lengths_gt4)


# =========================
# Задача 3: Обработка данных студентов (через генераторы списков)
# =========================
print(" Задача 3: Студенты ")

students = [
    {"name": "Радель", "age": 17, "grades": [4, 5, 4, 3]},
    {"name": "Егор", "age": 17, "grades": [3, 4, 3, 5]},
    {"name": "Адель", "age": 17, "grades": [5, 5, 5, 5]},
    {"name": "Александр", "age": 17, "grades": [4, 4, 3, 4]},
    {"name": "Саня", "age": 17, "grades": [3, 3, 4, 3]},
]

# 1) Список имен всех студентов
names = [s["name"] for s in students]
print("Имена:", names)

# 2) Список студентов старше 20 лет
older_20 = [s["name"] for s in students if s["age"] > 20]
print("Старше 20:", older_20)

# 3) Средний балл каждого студента (список чисел)
avg_each = [sum(s["grades"]) / len(s["grades"]) for s in students]
print("Средний балл каждого:", avg_each)

# 4) Список студентов со средним баллом выше 4.0
above_4 = [s["name"] for s in students if (sum(s["grades"]) / len(s["grades"])) > 4.0]
print("Средний > 4.0:", above_4)

# 5) Список строк "Имя (возраст): средний_балл"
info = [f'{s["name"]} ({s["age"]}): {sum(s["grades"]) / len(s["grades"]):.2f}' for s in students]
print("Строки:")
for line in info:
    print(" ", line)


# =========================
# Задача 4: Матрица 5x5 (дополнительно)
# =========================
print("Задача 4: Матрица 5x5")

n = 5

# 1) Матрица 5x5 из нулей
matrix = [[0 for _ in range(n)] for _ in range(n)]

# 2) Главная диагональ = 1
matrix = [[(1 if i == j else 0) for j in range(n)] for i in range(n)]

# 3) Побочная диагональ = 2 (если пересечение с главной — ставим 2, можно и иначе)
matrix = [[(2 if i + j == n - 1 else matrix[i][j]) for j in range(n)] for i in range(n)]

print("Матрица:")
for row in matrix:
    print(row)

# 4) Список всех элементов > 0
positive_elements = [x for row in matrix for x in row if x > 0]
print("Элементы > 0:", positive_elements)

# 5) Транспонировать матрицу
transposed = [[matrix[j][i] for j in range(n)] for i in range(n)]
print("Транспонированная:")
for row in transposed:
    print(row)