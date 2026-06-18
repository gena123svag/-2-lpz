# -*- coding: utf-8 -*-
"""
ДЗ 4: Генераторы списков (list comprehensions)
Файл: lab3_generators.py
"""

def print_header(title: str) -> None:
    """Выводит заголовок раздела."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def task1_basic_generators() -> None:
    """Часть 1: Базовые генераторы списков."""
    print_header("ЧАСТЬ 1 — ЗАДАЧА 1: БАЗОВЫЕ ГЕНЕРАТОРЫ")

    # 1. Список кубов чисел от 1 до 5
    cubes = [x ** 3 for x in range(1, 6)]
    print(f"1) Кубы чисел 1-5: {cubes}")
    print("   Ожидаемый результат: [1, 8, 27, 64, 125]")

    # 2. Список четных чисел от 0 до 20
    evens = [x for x in range(21) if x % 2 == 0]
    print(f"\n2) Четные числа 0-20: {evens}")
    print(f"   Первые 5: {evens[:5]}...")

    # 3. Список символов строки в верхнем регистре
    text = "python"
    uppercase_chars = [char.upper() for char in text]
    print(f"\n3) Символы '{text}' в верхнем регистре: {uppercase_chars}")

    # 4. Список длин слов
    words = ["яблоко", "банан", "апельсин", "киви"]
    lengths = [len(word) for word in words]
    print(f"\n4) Длины слов {words}: {lengths}")

    # 5. Преобразование типов
    numbers_str = ["1", "2", "3", "4", "5"]
    numbers_int = [int(x) for x in numbers_str]
    print(f"\n5) Преобразование {numbers_str} в int: {numbers_int}")


def task2_conditional_generators() -> None:
    """Часть 2.1: Генераторы списков с условиями (if)."""
    print_header("ЧАСТЬ 2 — ЗАДАЧА 2: ГЕНЕРАТОРЫ С УСЛОВИЯМИ (IF)")

    numbers = list(range(1, 21))
    print(f"Исходный список: {numbers}")

    # 1. Числа, делящиеся на 3
    divisible_by_3 = [x for x in numbers if x % 3 == 0]
    print(f"\n1) Числа, делящиеся на 3: {divisible_by_3}")

    # 2. Числа больше 10
    greater_than_10 = [x for x in numbers if x > 10]
    print(f"\n2) Числа больше 10: {greater_than_10}")

    # 3. Числа между 5 и 15
    between_5_15 = [x for x in numbers if 5 <= x <= 15]
    print(f"\n3) Числа от 5 до 15: {between_5_15}")

    # 4. Слова длиннее 4 букв
    fruits = ["яблоко", "груша", "банан", "апельсин", "киви", "арбуз"]
    long_fruits = [fruit for fruit in fruits if len(fruit) > 4]
    print(f"\n4) Фрукты длиннее 4 букв: {long_fruits}")

    # 5. Слова, начинающиеся с гласной
    vowels = "аеёиоуыэюя"
    names = ["анна", "борис", "елена", "иван", "ольга", "юрий"]
    vowel_words = [word for word in names if word[0].lower() in vowels]
    print(f"\n5) Слова на гласную: {vowel_words}")


def task3_if_else_generators() -> None:
    """Часть 2.2: Генераторы с if-else в выражении."""
    print_header("ЧАСТЬ 2 — ЗАДАЧА 3: IF-ELSE В ГЕНЕРАТОРАХ")

    numbers = list(range(1, 11))
    print(f"Исходный список: {numbers}")

    # 1. Четные/нечетные
    parity = ["четное" if x % 2 == 0 else "нечетное" for x in numbers]
    print("\n1) Четность чисел:")
    for i in range(len(numbers)):
        print(f"   {numbers[i]} — {parity[i]}")

    # 2. Оценки: сдал/не сдал
    grades = [3, 5, 4, 2, 5, 3, 4, 5]
    results = ["сдал" if grade >= 4 else "не сдал" for grade in grades]
    print(f"\n2) Результаты по оценкам {grades}:")
    print(f"   {results}")

    # 3. Положительные/отрицательные/ноль
    mixed_numbers = [-5, 10, 0, -3, 7, 0, -1]
    signs = ["+" if x > 0 else "-" if x < 0 else "0" for x in mixed_numbers]
    print(f"\n3) Знаки чисел {mixed_numbers}:")
    print(f"   {signs}")

    # 4. Температурные зоны (сравнение цикл vs генератор)
    temperatures = [-10, 0, 10, 20, 30, 40]
    zones = []
    for t in temperatures:
        if t < 0:
            zones.append("мороз")
        elif t < 15:
            zones.append("прохладно")
        elif t < 25:
            zones.append("тепло")
        else:
            zones.append("жарко")

    zones_lc = [
        "мороз" if t < 0 else
        "прохладно" if t < 15 else
        "тепло" if t < 25 else
        "жарко"
        for t in temperatures
    ]

    print(f"\n4) Температурные зоны для {temperatures}:")
    print(f"   Через цикл:      {zones}")
    print(f"   Через генератор: {zones_lc}")


def task4_matrix_generators() -> None:
    """Часть 3.1: Матрицы и вложенные генераторы."""
    print_header("ЧАСТЬ 3 — ЗАДАЧА 4: МАТРИЦЫ И ВЛОЖЕННЫЕ ГЕНЕРАТОРЫ")

    # 1. Создание матрицы 3x3
    matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
    print("1) Матрица 3x3:")
    for row in matrix:
        print(f"   {row}")

    # 2. Таблица умножения 5x5
    multiplication_table = [[(i + 1) * (j + 1) for j in range(5)] for i in range(5)]
    print("\n2) Таблица умножения 5x5:")
    for i, row in enumerate(multiplication_table, start=1):
        print(f"   {i}: {row}")

    # 3. "Расплющивание" матрицы
    flat_matrix = [num for row in matrix for num in row]
    print(f"\n3) Расплющенная матрица: {flat_matrix}")

    # 4. Транспонирование матрицы
    transposed = [[matrix[j][i] for j in range(3)] for i in range(3)]
    print("\n4) Транспонированная матрица:")
    for row in transposed:
        print(f"   {row}")

    # 5. Диагональ матрицы
    diagonal = [matrix[i][i] for i in range(3)]
    print(f"\n5) Главная диагональ: {diagonal}")


def task5_nested_loops() -> None:
    """Часть 3.2: Вложенные циклы в генераторах."""
    print_header("ЧАСТЬ 3 — ЗАДАЧА 5: ВЛОЖЕННЫЕ ЦИКЛЫ")

    # 1. Все пары чисел
    pairs = [(x, y) for x in range(1, 4) for y in range(1, 4)]
    print(f"1) Все пары чисел от 1 до 3: {pairs}")

    # 2. Декартово произведение
    colors = ["красный", "зеленый", "синий"]
    sizes = ["S", "M", "L"]
    products = [f"{color} {size}" for color in colors for size in sizes]
    print("\n2) Декартово произведение цветов и размеров:")
    for product in products:
        print(f"   {product}")

    # 3. Таблица умножения в виде строк
    table_strings = [f"{i} x {j} = {i*j}" for i in range(1, 4) for j in range(1, 4)]
    print("\n3) Таблица умножения как строки:")
    for i in range(0, 9, 3):
        print(f"   {table_strings[i:i+3]}")


def task6_student_data() -> None:
    """Часть 4.1: Обработка данных студентов через генераторы."""
    print_header("ЧАСТЬ 4 — ЗАДАЧА 6: ОБРАБОТКА ДАННЫХ СТУДЕНТОВ")

    students = [
        {"name": "Анна", "age": 20, "grades": [4, 5, 4, 3], "group": "ПИН-231"},
        {"name": "Борис", "age": 19, "grades": [3, 4, 3, 5], "group": "ПИН-232"},
        {"name": "Виктор", "age": 21, "grades": [5, 5, 5, 5], "group": "ПИН-231"},
        {"name": "Галина", "age": 20, "grades": [4, 4, 3, 4], "group": "ПИН-233"},
        {"name": "Дмитрий", "age": 22, "grades": [3, 3, 4, 3], "group": "ПИН-232"},
    ]

    # 1. Имена всех студентов
    names = [s["name"] for s in students]
    print(f"1) Имена студентов: {names}")

    # 2. Средний балл каждого студента
    averages = [sum(s["grades"]) / len(s["grades"]) for s in students]
    print(f"\n2) Средние баллы: {averages}")

    # 3. Имена студентов старше 20
    older_names = [s["name"] for s in students if s["age"] > 20]
    print(f"\n3) Студенты старше 20 лет: {older_names}")

    # 4. Студенты со средним баллом выше 4.0
    good_students = [
        s["name"]
        for s in students
        if (sum(s["grades"]) / len(s["grades"])) > 4.0
    ]
    print(f"\n4) Студенты со средним баллом > 4.0: {good_students}")

    # 5. Строки формата "Имя (Группа): средний_балл"
    student_info = [
        f"{s['name']} ({s['group']}): {sum(s['grades'])/len(s['grades']):.2f}"
        for s in students
    ]
    print("\n5) Информация о студентах:")
    for info in student_info:
        print(f"   {info}")

    # 6. Группировка по группам (как в методичке — через обычный цикл)
    groups = {}
    for s in students:
        group = s["group"]
        if group not in groups:
            groups[group] = []
        groups[group].append(s["name"])

    print("\n6) Студенты по группам:")
    for group, members in groups.items():
        print(f"   {group}: {members}")


def task7_real_world_examples() -> None:
    """Часть 4.2: Практические примеры."""
    print_header("ЧАСТЬ 4 — ЗАДАЧА 7: ПРАКТИЧЕСКИЕ ПРИМЕРЫ")

    # 1. Очистка данных
    raw_data = ["  Иван ", "ПЕТР ", "  Мария  ", "АННА"]
    cleaned = [name.strip().title() for name in raw_data]
    print(f"1) Очищенные имена: {raw_data} → {cleaned}")

    # 2. Фильтрация валидных email
    emails = [
        "user@example.com",
        "invalid-email",
        "test@gmail.com",
        "no-at-sign",
        "hello@domain.ru",
    ]
    valid_emails = [email for email in emails if "@" in email and "." in email]
    print(f"\n2) Валидные email: {valid_emails}")

    # 3. Конвертация валют
    exchange_rate = 90  # руб за доллар
    prices_usd = [10, 20, 50, 100]
    prices_rub = [price * exchange_rate for price in prices_usd]
    print(f"\n3) Цены в рублях: {prices_usd} USD → {prices_rub} RUB")

    # 4. Генерация паролей
    import random
    import string
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    passwords = ["".join(random.choice(chars) for _ in range(12)) for _ in range(5)]
    print("\n4) Сгенерированные пароли:")
    for i, pwd in enumerate(passwords, 1):
        print(f"   Пароль {i}: {pwd}")

    # 5. Анализ текста
    text = "Python — это мощный и простой язык программирования. Python популярен."
    words = text.lower().replace(".", "").replace("—", "").split()

    long_words = [word for word in words if len(word) > 3]
    unique_words = list({word for word in words})

    print("\n5) Анализ текста:")
    print(f"   Все слова: {len(words)}")
    print(f"   Слова длиннее 3 букв: {len(long_words)}")
    print(f"   Уникальные слова: {len(unique_words)}")
    print(f"   Пример уникальных: {unique_words[:5]}...")


def main() -> None:
    print("=" * 60)
    print("ДЗ 4: ГЕНЕРАТОРЫ СПИСКОВ (LIST COMPREHENSIONS)")
    print("=" * 60)

    task1_basic_generators()
    task2_conditional_generators()
    task3_if_else_generators()
    task4_matrix_generators()
    task5_nested_loops()
    task6_student_data()
    task7_real_world_examples()

    print("\n" + "=" * 60)
    print("РАБОТА ЗАВЕРШЕНА!")
    print("=" * 60)


if __name__ == "__main__":
    main()