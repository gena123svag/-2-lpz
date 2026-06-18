# lab1_refactored.py (шаг 1: переименование)
STUDENT_GRADES = [5, 3, 4, 2, 5, 4, 3, 5, 4, 2, 3, 4, 5, 4, 3, 2, 5, 4, 3, 4, 5]

def calculate_average_grade():
    """Вычисляет средний балл из списка оценок."""
    total = 0
    for grade in STUDENT_GRADES:
        total = total + grade
    average_grade = total / len(STUDENT_GRADES)
    return average_grade

def find_min_max_grades():
    """Находит минимальную и максимальную оценку."""
    max_grade = STUDENT_GRADES[0]
    min_grade = STUDENT_GRADES[0]
    for grade in STUDENT_GRADES:
        if grade > max_grade:
            max_grade = grade
        if grade < min_grade:
            min_grade = grade
    return min_grade, max_grade

def count_grade_occurrences(target_grade):
    """Считает, сколько раз встречается указанная оценка."""
    count = 0
    for grade in STUDENT_GRADES:
        if grade == target_grade:
            count = count + 1
    return count

def display_grade_statistics():
    """Выводит статистику (заголовок)."""
    print("Анализ оценок")

# Основной блок программы
average = calculate_average_grade()
print(f"Средний балл: {average:.2f}")

min_grade, max_grade = find_min_max_grades()
print(f"Максимальная оценка: {max_grade}")
print(f"Минимальная оценка: {min_grade}")

print("Количество каждой оценки:")
for grade_value in range(2, 6):
    # Здесь пока сохраняется исходная ошибка: выводится grade_value, а не реальное количество
    print(f"Оценка {grade_value}: {grade_value} раз")

if __name__ == "__main__":
    display_grade_statistics()