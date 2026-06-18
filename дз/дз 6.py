# -*- coding: utf-8 -*-
"""
ДЗ 6. Практика: Множества + Кортежи
(множества — по примерам из методички; кортежи — базовая практика)
"""

from __future__ import annotations
import random


def header(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# =========================
# ЧАСТЬ 1 — МНОЖЕСТВА (set)
# =========================
def task_set_1_remove_duplicates() -> None:
    header("МНОЖЕСТВА — Пример 1: удаление дубликатов из списка")

    grades = [4, 5, 3, 4, 5, 4, 3, 5, 4]
    unique_grades = list(set(grades))

    print(f"Исходные оценки: {grades}")
    print(f"Уникальные оценки: {unique_grades}  (порядок может быть другим)")

    # С сохранением порядка (Python 3.7+)
    words = ["яблоко", "банан", "яблоко", "апельсин", "банан"]
    unique_ordered = list(dict.fromkeys(words))
    print(f"Уникальные с сохранением порядка: {unique_ordered}")


def find_common_friends(*friend_lists: list[str]) -> set[str]:
    """Находит друзей, которые есть у всех списков."""
    if not friend_lists:
        return set()

    common = set(friend_lists[0])
    for friends in friend_lists[1:]:
        common &= set(friends)
    return common


def task_set_2_common_friends() -> None:
    header("МНОЖЕСТВА — Пример 2: общие друзья (пересечение)")

    alice_friends = ["Егор", "Радель", "Адель", "Саня"]
    bob_friends = ["Радель", "Галина", "Саня", "Елена"]
    carol_friends = ["Виктор", "Егор", "Саня", "Федор"]

    common = find_common_friends(alice_friends, bob_friends, carol_friends)
    print("Общие друзья всех троих:", common)


def has_duplicates(data: list[str]) -> bool:
    """Проверяет, есть ли дубликаты."""
    return len(data) != len(set(data))


def task_set_3_duplicates_check() -> None:
    header("МНОЖЕСТВА — Пример 3: проверка уникальности данных")

    students = ["Иван", "Петр", "Анна", "Иван", "Мария"]
    if has_duplicates(students):
        print("⚠Внимание! Есть повторяющиеся имена!")
        unique_students = set(students)
        duplicates = len(students) - len(unique_students)
        print(f"Найдено {duplicates} дубликат(ов)")
        print("Уникальные имена:", unique_students)
    else:
        print("Все имена уникальны!")

    phones = ["+79178893804", "+79003208959", "+79325935346", "+79006802942"]
    if has_duplicates(phones):
        print("⚠Обнаружены повторяющиеся номера!")
        print("Уникальные номера:", set(phones))


def task_set_4_lottery() -> None:
    header("МНОЖЕСТВА — Пример 4: генератор уникальных случайных чисел (лотерея)")

    # Вариант 1: через set + while
    lottery_numbers = set()
    while len(lottery_numbers) < 6:
        lottery_numbers.add(random.randint(1, 49))
    print("Лотерейные числа (вариант 1):", sorted(lottery_numbers))

    # Вариант 2: random.sample
    lottery_numbers2 = set(random.sample(range(1, 50), 6))
    print("Лотерейные числа (вариант 2):", sorted(lottery_numbers2))


def task_set_5_text_analysis() -> None:
    header("МНОЖЕСТВА — Пример 5: анализ текста")

    text = "Мама мыла раму, а рама мыла маму"

    letters = set(text.lower())
    print("Уникальные символы:", letters)

    russian_letters = {ch for ch in letters if "а" <= ch <= "я"}
    print("Русские буквы в тексте:", russian_letters)

    text1 = "быстрая коричневая лиса"
    text2 = "ленивая коричневая собака"

    set1 = set(text1.replace(" ", ""))
    set2 = set(text2.replace(" ", ""))

    common_letters = set1 & set2
    print("Общие буквы (text1 & text2):", common_letters)


# =========================
# ЧАСТЬ 2 — КОРТЕЖИ (tuple)
# =========================
def task_tuples_basic() -> None:
    header("КОРТЕЖИ — базовые операции")

    # 1) Создание кортежа
    t = ("Анна", 20, "ПИН-231")
    print("Кортеж:", t)

    # 2) Индексация / срезы
    print("t[0] =", t[0])
    print("t[1:] =", t[1:])

    # 3) Длина
    print("len(t) =", len(t))

    # 4) Распаковка
    name, age, group = t
    print("Распаковка:", name, age, group)

    # 5) Обмен переменных (часто показывают с кортежем)
    a, b = 10, 20
    a, b = b, a
    print("Обмен a и b:", a, b)

    # 6) Конкатенация кортежей
    t2 = ("Python", "SQL")
    print("t + t2 =", t + t2)

    # 7) Преобразование list <-> tuple
    lst = [1, 2, 2, 3]
    as_tuple = tuple(lst)
    back_to_list = list(as_tuple)
    print("list -> tuple:", as_tuple)
    print("tuple -> list:", back_to_list)

    # 8) Методы кортежа: count / index
    nums = (1, 2, 2, 3, 2)
    print("nums.count(2) =", nums.count(2))
    print("nums.index(3) =", nums.index(3))


def task_tuples_as_keys_and_sorting() -> None:
    header("КОРТЕЖИ — кортеж как ключ и сортировка списка кортежей")

    # 1) Кортеж как ключ словаря (потому что tuple неизменяемый)
    coords = {(0, 0): "start", (1, 2): "point A", (5, 3): "point B"}
    print("Словарь с ключами-кортежами:", coords)
    print("coords[(1, 2)] =", coords[(1, 2)])

    # 2) Список кортежей и сортировка по 2-му элементу
    students = [("Егор", 4.25), ("Радель", 3.75), ("Саня", 5.0), ("Адель", 4.0)]
    print("До сортировки:", students)

    students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
    print("Сортировка по среднему (убыв.):", students_sorted)


def main() -> None:
    # Множества (по примерам из файла)
    task_set_1_remove_duplicates()
    task_set_2_common_friends()
    task_set_3_duplicates_check()
    task_set_4_lottery()
    task_set_5_text_analysis()

    # Кортежи (практика)
    task_tuples_basic()
    task_tuples_as_keys_and_sorting()

    header("ГОТОВО")


if __name__ == "__main__":
    main()