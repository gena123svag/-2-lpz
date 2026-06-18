# -*- coding: utf-8 -*-
import datetime

# ============================
# 1. Подготовка данных
# ============================
# Файл students.txt должен лежать в той же папке

# ============================
# 2. Чтение данных из файла
# ============================
print("=" * 50)
print("ШАГ 2: Чтение данных из файла")
print("=" * 50)

try:
    with open('students.txt', 'r', encoding='utf-8') as file:
        file_lines = file.readlines()
    print("Содержимое файла students.txt:")
    print("-" * 30)
    for i, line in enumerate(file_lines, 1):
        print(f"{i}: {line.strip()}")
except FileNotFoundError:
    print("Ошибка: файл students.txt не найден!")
    exit()

# ============================
# 3. Базовая обработка и парсинг
# ============================
print("\n" + "=" * 50)
print("ШАГ 3: Парсинг строк")
print("=" * 50)

all_students_raw = []
for line in file_lines:
    clean_line = line.strip()
    if not clean_line:
        continue
    parts = clean_line.split('; ')
    student_name = parts[0]
    grades_list = parts[1:]
    all_students_raw.append({
        'name': student_name,
        'grades_raw': grades_list
    })
    print(f"Студент: {student_name}")
    print(f"  Список оценок (сырой): {grades_list}")

# ============================
# 4. Структурирование данных
# ============================
print("\n" + "=" * 50)
print("ШАГ 4: Структурированные данные")
print("=" * 50)

students = []   # список словарей вида {'name': 'Имя', 'Предмет': оценка, ...}
for student_raw in all_students_raw:
    student_dict = {'name': student_raw['name']}
    for grade_item in student_raw['grades_raw']:
        subject, grade_str = grade_item.split('=')
        grade = int(grade_str)
        student_dict[subject] = grade
    students.append(student_dict)

# Вывод структурированных данных
for student in students:
    print(f"\nДанные студента: {student['name']}")
    for subject, grade in student.items():
        if subject != 'name':
            print(f"  {subject}: {grade}")

# ============================
# 5. Фильтрация по предмету
# ============================
print("\n" + "=" * 50)
print("ШАГ 5: Фильтрация студентов по предмету")
print("=" * 50)

target_subject = input("Введите название предмета для анализа: ").strip()
filtered_students = []   # список кортежей (имя, оценка)

for student in students:
    if target_subject in student:
        filtered_students.append((student['name'], student[target_subject]))

if filtered_students:
    print(f"\nНайден {len(filtered_students)} студент(ов) с предметом '{target_subject}':")
    print("-" * 40)
    for name, grade in filtered_students:
        print(f"{name}: {grade} баллов")
else:
    print(f"\nПредмет '{target_subject}' не найден у студентов.")

# ============================
# 6. Статистика по предмету
# ============================
print("\n" + "-" * 50)
print("ШАГ 6: Статистика по предмету")
print("=" * 50)

if filtered_students:
    grades_only = [grade for _, grade in filtered_students]
    avg_grade = sum(grades_only) / len(grades_only)
    max_grade = max(grades_only)
    min_grade = min(grades_only)
    count_students = len(grades_only)

    print(f"Статистика по предмету '{target_subject}':")
    print(f"  • Количество студентов: {count_students}")
    print(f"  • Средний балл: {avg_grade:.2f}")
    print(f"  • Максимальный балл: {max_grade}")
    print(f"  • Минимальный балл: {min_grade}")

    top_students = [name for name, grade in filtered_students if grade == max_grade]
    print(f"  • Лучшие студенты: {', '.join(top_students)}")
else:
    print(f"Невозможно вычислить статистику: предмет '{target_subject}' не найден.")

# ============================
# 7. Запись результатов в файл
# ============================
print("\n" + "-" * 50)
print("ШАГ 7: Запись результатов в файл")
print("=" * 50)

result_content = []
result_content.append("=" * 50)
result_content.append(f"АНАЛИЗ УСПЕВАЕМОСТИ ПО ПРЕДМЕТУ: {target_subject}")
result_content.append("=" * 50)
result_content.append("")

if filtered_students:
    result_content.append("СПИСОК СТУДЕНТОВ:")
    result_content.append("-" * 30)
    for name, grade in filtered_students:
        result_content.append(f"• {name}: {grade} баллов")
else:
    result_content.append(f"Студентов с предметом '{target_subject}' не найдено.")

result_content.append("")
if filtered_students:
    result_content.append("СТАТИСТИКА:")
    result_content.append("-" * 30)
    result_content.append(f"Количество студентов: {count_students}")
    result_content.append(f"Средний балл: {avg_grade:.2f}")
    result_content.append(f"Максимальный балл: {max_grade}")
    result_content.append(f"Минимальный балл: {min_grade}")
    result_content.append("")
    result_content.append(f"Дата анализа: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}")

try:
    with open('analysis_result.txt', 'w', encoding='utf-8') as result_file:
        for line in result_content:
            result_file.write(line + '\n')
    print("Результаты успешно записаны в файл 'analysis_result.txt'")
except Exception as e:
    print(f"Ошибка при записи в файл: {e}")

# ============================
# 8. Дополнительное задание
# ============================
print("\n" + "=" * 50)
print("ШАГ 8: Дополнительный анализ")
print("=" * 50)

# 8.1. Предмет с самым высоким средним баллом
subject_grades = {}  # предмет -> список оценок
for student in students:
    for subject, grade in student.items():
        if subject != 'name':
            subject_grades.setdefault(subject, []).append(grade)

if subject_grades:
    avg_by_subject = {subj: sum(grades)/len(grades) for subj, grades in subject_grades.items()}
    best_subject = max(avg_by_subject, key=avg_by_subject.get)
    print(f"Предмет с самым высоким средним баллом: '{best_subject}' ({avg_by_subject[best_subject]:.2f})")
else:
    print("Нет данных для расчёта.")

# 8.2. Студент с наибольшим средним баллом по всем предметам
student_avg = {}
for student in students:
    grades = [grade for subj, grade in student.items() if subj != 'name']
    if grades:
        student_avg[student['name']] = sum(grades) / len(grades)

if student_avg:
    best_student = max(student_avg, key=student_avg.get)
    print(f"Студент с наибольшим средним баллом: '{best_student}' ({student_avg[best_student]:.2f})")
else:
    print("Нет данных для расчёта.")

# 8.3. Рейтинг студентов по среднему баллу (по убыванию)
if student_avg:
    sorted_students = sorted(student_avg.items(), key=lambda x: x[1], reverse=True)
    print("\nРейтинг студентов по среднему баллу:")
    for rank, (name, avg) in enumerate(sorted_students, 1):
        print(f"{rank}. {name} – {avg:.2f}")
else:
    print("Нет данных для рейтинга.")