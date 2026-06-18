def input_student_grades():
    ''' ввод данных (оценки) '''
    grades = []
    print("введите оценки студентов (от 2 до 5).")
    print("0 - завершить ввод оценок")

    while True:
        try:
            grade = int(input("введите оценку: "))
            if grade == 0:
                break
            if grade < 2 or grade > 5:
                print("оценка должна быть от 2 до 5.")
                continue
            grades.append(grade)
        except ValueError:
            print("введите целое число.")

    return grades


def calculate_average_grade(grades):
    """вычесляем средний бал оценок которые ввели"""
    if not grades:
        return 0
    return sum(grades) / len(grades)


def find_min_max_grades(grades):
    """находим макс. и мин. оценки в классе"""
    if not grades:
        return None, None
    return min(grades), max(grades)


def count_grade_occurrences(grades, grade_value):
    """счет, сколько раз какая оценка встречается ."""
    count = 0
    for grade in grades:
        if grade == grade_value:
            count += 1
    return count


def find_most_frequent_grade(grades):
    """находим самую частую оценку (мода)."""
    if not grades:
        return None

    grade_count = {}

    for grade in grades:
        if grade in grade_count:
            grade_count[grade] += 1
        else:
            grade_count[grade] = 1

    most_frequent_grade = None
    max_count = 0

    for grade, count in grade_count.items():
        if count > max_count:
            max_count = count
            most_frequent_grade = grade

    return most_frequent_grade


def visualize_grade_distribution(grades):
    """гистограмма"""
    if not grades:
        print("нет данных")
        return

    grade_count = {}
    for grade in grades:
        grade_count[grade] = grade_count.get(grade, 0) + 1

    max_count = max(grade_count.values())

    print("\nГистограмма распределения оценок:")
    print("─" * 50)

    for grade in sorted(grade_count.keys()):
        count = grade_count[grade]
        bar_length = int((count / max_count) * 40)
        bar = "█" * bar_length
        print(f"Оценка {grade}: {bar} {count} ({count / len(grades) * 100:.1f}%)")

    most_frequent = find_most_frequent_grade(grades)
    print(f"\n👑 Самая частая оценка: {most_frequent}")
    print("─" * 50)


def display_grade_statistics():
    """Выводит статистику по оценкам."""
    print("=" * 50)
    print("АНАЛИЗ ОЦЕНОК СТУДЕНТОВ")
    print("=" * 50)

    MIN_POSSIBLE_GRADE = 2
    MAX_POSSIBLE_GRADE = 5

    average = calculate_average_grade(STUDENT_GRADES)
    min_grade, max_grade = find_min_max_grades(STUDENT_GRADES)
    most_frequent = find_most_frequent_grade(STUDENT_GRADES)

    print(f"\n1. Средний балл группы: {average:.2f}")
    print(f"2. Минимальная оценка в группе: {min_grade}")
    print(f"3. Максимальная оценка в группе: {max_grade}")
    print(f"4. Самая частая оценка: {most_frequent}")

    print("\n5. Распределение оценок:")
    print("-" * 25)

    for grade_value in range(MIN_POSSIBLE_GRADE, MAX_POSSIBLE_GRADE + 1):
        occurrences = count_grade_occurrences(STUDENT_GRADES, grade_value)
        percentage = (occurrences / len(STUDENT_GRADES)) * 100
        print(f"   Оценка {grade_value}: {occurrences:2d} студент(ов) ({percentage:.1f}%)")

    visualize_grade_distribution(STUDENT_GRADES)

    print("\n" + "=" * 50)


def main():
    global STUDENT_GRADES
    STUDENT_GRADES = input_student_grades()

    display_grade_statistics()


if __name__ == "__main__":
    main()
