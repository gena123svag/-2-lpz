"""
Модуль для анализа успеваемости студентов.

Содержит функции для вычисления статистики по оценкам.
"""

# Исходные данные
STUDENT_GRADES = [5, 3, 4, 2, 5, 4, 3, 5, 4, 2, 3, 4, 5, 4, 3, 2, 5, 4, 3, 4, 5]

# Константы для диапазона оценок (избавляемся от «магических чисел»)
MIN_POSSIBLE_GRADE = 2
MAX_POSSIBLE_GRADE = 5


def calculate_average_grade(grades):
    """
    Вычисляет средний балл из списка оценок.

    Args:
        grades (list): Список оценок студентов.

    Returns:
        float: Средний балл. Если список пуст, возвращает 0.0.
    """
    if not grades:
        return 0.0

    total = 0
    for grade in grades:
        total += grade

    return total / len(grades)


def find_min_max_grades(grades):
    """
    Находит минимальную и максимальную оценку в списке.

    Args:
        grades (list): Список оценок для анализа.

    Returns:
        tuple: (минимальная_оценка, максимальная_оценка).

    Raises:
        ValueError: Если передан пустой список.
    """
    if not grades:
        raise ValueError("Список оценок не может быть пустым")

    min_grade = grades[0]
    max_grade = grades[0]

    for grade in grades:
        if grade > max_grade:
            max_grade = grade
        if grade < min_grade:
            min_grade = grade

    return min_grade, max_grade


def count_grade_occurrences(grades, target_grade):
    """
    Считает, сколько раз встречается заданная оценка.

    Args:
        grades (list): Список оценок для анализа.
        target_grade (int): Оценка, количество которой нужно посчитать.

    Returns:
        int: Количество вхождений заданной оценки.
    """
    count = 0
    for grade in grades:
        if grade == target_grade:
            count += 1
    return count


def display_grade_statistics():
    """Выводит полную статистику по оценкам студентов."""
    print("=" * 50)
    print("АНАЛИЗ УСПЕВАЕМОСТИ СТУДЕНТОВ")
    print("=" * 50)

    # Вычисляем статистику
    average = calculate_average_grade(STUDENT_GRADES)
    min_grade, max_grade = find_min_max_grades(STUDENT_GRADES)

    print(f"\n1. Средний балл группы: {average:.2f}")
    print(f"2. Минимальная оценка в группе: {min_grade}")
    print(f"3. Максимальная оценка в группе: {max_grade}")

    print("\n4. Распределение оценок:")
    print("-" * 25)

    total_students = len(STUDENT_GRADES)
    for grade_value in range(MIN_POSSIBLE_GRADE, MAX_POSSIBLE_GRADE + 1):
        occurrences = count_grade_occurrences(STUDENT_GRADES, grade_value)
        percentage = (occurrences / total_students) * 100
        print(f"   Оценка {grade_value}: {occurrences:2d} студент(ов) ({percentage:5.1f}%)")

    print("\n" + "=" * 50)


def main():
    """Основная точка входа в программу."""
    display_grade_statistics()


if __name__ == "__main__":
    main()