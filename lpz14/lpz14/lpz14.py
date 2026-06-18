import csv
import json
import re
from datetime import datetime
from collections import defaultdict

# ============================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ (для создания исходных данных)
# ============================================================

def create_initial_files():
    """Создаёт все необходимые исходные файлы для заданий."""
    # Задание 1: books.csv
    books_data = [
        ["Название", "Автор", "Год", "Жанр", "Цена"],
        ["Мастер и Маргарита", "Булгаков", "1967", "роман", "500"],
        ["Война и мир", "Толстой", "1869", "роман", "800"],
        ["Преступление и наказание", "Достоевский", "1866", "роман", "450"],
        ["Три товарища", "Ремарк", "1936", "роман", "600"],
        ["Колобок", "Народная", "1890", "сказка", "200"]
    ]
    with open("books.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(books_data)

    # Задание 2: employees.json
    employees_data = [
        {"name": "Иван", "hours": 160, "rate": 200, "department": "IT"},
        {"name": "Мария", "hours": 150, "rate": 250, "department": "HR"},
        {"name": "Петр", "hours": 170, "rate": 180, "department": "IT"},
        {"name": "Ольга", "hours": 140, "rate": 300, "department": "Sales"},
        {"name": "Анна", "hours": 180, "rate": 220, "department": "IT"},
        {"name": "Сергей", "hours": 120, "rate": 150, "department": "Sales"}
    ]
    with open("employees.json", "w", encoding="utf-8") as f:
        json.dump(employees_data, f, ensure_ascii=False, indent=2)

    # Задание 3: sales.csv
    sales_data = [
        ["Дата", "Товар", "Количество", "Цена"],
        ["2026-04-01", "Ноутбук", "2", "50000"],
        ["2026-04-01", "Мышь", "5", "1500"],
        ["2026-04-02", "Ноутбук", "1", "50000"],
        ["2026-04-02", "Клавиатура", "3", "3000"],
        ["2026-04-03", "Мышь", "10", "1500"],
        ["2026-04-03", "Ноутбук", "3", "50000"],
        ["2026-04-04", "Клавиатура", "2", "3000"],
        ["2026-04-05", "Мышь", "8", "1500"]
    ]
    with open("sales.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(sales_data)

    # Задание 4: students.csv
    students_data = [
        ["student_id", "name", "group"],
        ["1", "Иван Петров", "ПИН-231"],
        ["2", "Анна Сидорова", "ПИН-231"],
        ["3", "Петр Иванов", "ПИН-232"],
        ["4", "Мария Кузнецова", "ПИН-232"],
        ["5", "Алексей Смирнов", "ПИН-231"]
    ]
    with open("students.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(students_data)

    # Задание 4: grades.json
    grades_data = [
        {"student_id": 1, "subject": "Python", "grade": 5},
        {"student_id": 1, "subject": "Математика", "grade": 4},
        {"student_id": 2, "subject": "Python", "grade": 5},
        {"student_id": 2, "subject": "Математика", "grade": 5},
        {"student_id": 3, "subject": "Python", "grade": 3},
        {"student_id": 3, "subject": "Математика", "grade": 4},
        {"student_id": 4, "subject": "Python", "grade": 5},
        {"student_id": 4, "subject": "Математика", "grade": 5},
        {"student_id": 5, "subject": "Python", "grade": 4},
        {"student_id": 5, "subject": "Математика", "grade": 4}
    ]
    with open("grades.json", "w", encoding="utf-8") as f:
        json.dump(grades_data, f, ensure_ascii=False, indent=2)

    # Задание 5: dirty_data.csv
    dirty_data = [
        ["Имя", "Телефон", "Email", "Возраст"],
        ["Иван Петров", "+7-999-123-45-67", "ivan@mail.ru", "двадцать"],
        ["Анна Сидорова", "8-999-123-45-67", "anna@@gmail.com", "19"],
        ["Петр Иванов", "+7 999 123 45 67", "petr&mail.ru", "25 лет"],
        ["Мария Кузнецова", "89991234567", "maria@", "20"],
        ["Алексей Смирнов", "+7-999-1234567", "alexey@mail.ru", "21"]
    ]
    with open("dirty_data.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(dirty_data)

    print("✅ Все исходные файлы созданы.\n")

# ============================================================
# ЗАДАНИЕ 1: Конвертер для списка книг (3 балла)
# ============================================================

def task1_books():
    """
    Читает books.csv, добавляет поля:
    - Скидка = 10% от цены
    - Цена_со_скидкой = цена - скидка
    - Век (19, 20, 21) по году издания
    Сохраняет в books_discount.json
    """
    print("\n--- Задание 1: Книги ---")
    try:
        with open("books.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            books = []
            for row in reader:
                price = float(row["Цена"])
                discount = price * 0.1
                price_with_discount = price - discount
                year = int(row["Год"])
                century = (year - 1) // 100 + 1  # 1901-2000 -> 20, etc.
                # Века 19,20,21 для годов 1801-2100
                if century < 19:
                    century = 19
                elif century > 21:
                    century = 21
                book = {
                    "Название": row["Название"],
                    "Автор": row["Автор"],
                    "Год": year,
                    "Жанр": row["Жанр"],
                    "Цена": price,
                    "Скидка": discount,
                    "Цена_со_скидкой": round(price_with_discount, 2),
                    "Век": century
                }
                books.append(book)
        with open("books_discount.json", "w", encoding="utf-8") as f:
            json.dump(books, f, ensure_ascii=False, indent=2)
        print(f"✅ Сохранено {len(books)} книг в books_discount.json")
    except Exception as e:
        print(f"❌ Ошибка в задании 1: {e}")

# ============================================================
# ЗАДАНИЕ 2: Конвертер для списка сотрудников (3 балла)
# ============================================================

def task2_employees():
    """
    Читает employees.json, добавляет:
    - salary = hours * rate
    - bonus = 10% от salary (для Sales 5%)
    - total_salary = salary + bonus
    Фильтрует total_salary > 30000
    Сортирует по total_salary (убывание)
    Сохраняет в employees_filtered.csv
    """
    print("\n--- Задание 2: Сотрудники ---")
    try:
        with open("employees.json", "r", encoding="utf-8") as f:
            employees = json.load(f)
        for emp in employees:
            salary = emp["hours"] * emp["rate"]
            if emp["department"] == "Sales":
                bonus = salary * 0.05
            else:
                bonus = salary * 0.10
            total_salary = salary + bonus
            emp["salary"] = salary
            emp["bonus"] = bonus
            emp["total_salary"] = total_salary
        # Фильтрация
        filtered = [emp for emp in employees if emp["total_salary"] > 30000]
        # Сортировка
        filtered.sort(key=lambda x: x["total_salary"], reverse=True)
        # Сохранение в CSV
        if filtered:
            headers = ["name", "hours", "rate", "department", "salary", "bonus", "total_salary"]
            with open("employees_filtered.csv", "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(filtered)
            print(f"✅ Отфильтровано {len(filtered)} сотрудников (из {len(employees)})")
        else:
            print("⚠ Нет сотрудников с total_salary > 30000")
    except Exception as e:
        print(f"❌ Ошибка в задании 2: {e}")

# ============================================================
# ЗАДАНИЕ 3: Анализ продаж (4 балла)
# ============================================================

def task3_sales():
    """
    Анализирует sales.csv:
    - добавляет поле Выручка
    - группирует по товарам: общее количество и общая выручка
    - находит товар с максимальной выручкой
    - находит день с максимальной выручкой
    - сохраняет sales_summary.json и sales_by_product.csv
    """
    print("\n--- Задание 3: Анализ продаж ---")
    try:
        with open("sales.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            sales = []
            for row in reader:
                qty = int(row["Количество"])
                price = int(row["Цена"])
                revenue = qty * price
                sales.append({
                    "Дата": row["Дата"],
                    "Товар": row["Товар"],
                    "Количество": qty,
                    "Цена": price,
                    "Выручка": revenue
                })
        # Группировка по товарам
        product_stats = defaultdict(lambda: {"quantity": 0, "revenue": 0})
        for s in sales:
            prod = s["Товар"]
            product_stats[prod]["quantity"] += s["Количество"]
            product_stats[prod]["revenue"] += s["Выручка"]
        # Товар с максимальной выручкой
        best_product = max(product_stats.items(), key=lambda x: x[1]["revenue"])
        best_product_name, best_product_data = best_product
        # День с максимальной выручкой
        day_revenue = defaultdict(int)
        for s in sales:
            day_revenue[s["Дата"]] += s["Выручка"]
        best_day = max(day_revenue.items(), key=lambda x: x[1])
        # Общая статистика
        total_revenue = sum(product_stats[p]["revenue"] for p in product_stats)
        total_items = sum(product_stats[p]["quantity"] for p in product_stats)
        summary = {
            "total_revenue": total_revenue,
            "total_items_sold": total_items,
            "best_product": best_product_name,
            "best_product_revenue": best_product_data["revenue"],
            "best_day": best_day[0],
            "best_day_revenue": best_day[1]
        }
        with open("sales_summary.json", "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        # Статистика по товарам в CSV
        product_rows = []
        for prod, stats in product_stats.items():
            product_rows.append({
                "Товар": prod,
                "Количество": stats["quantity"],
                "Выручка": stats["revenue"]
            })
        with open("sales_by_product.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Товар", "Количество", "Выручка"])
            writer.writeheader()
            writer.writerows(product_rows)
        print(f"✅ Сохранены sales_summary.json и sales_by_product.csv")
        print(f"   Лучший товар: {best_product_name} ({best_product_data['revenue']} руб.)")
        print(f"   Лучший день: {best_day[0]} ({best_day[1]} руб.)")
    except Exception as e:
        print(f"❌ Ошибка в задании 3: {e}")

# ============================================================
# ЗАДАНИЕ 4: Объединение данных из двух файлов (5 баллов)
# ============================================================

def task4_merge():
    """
    Объединяет students.csv и grades.json по student_id.
    Добавляет каждому студенту: список оценок, средний балл, статус.
    Вычисляет средний балл по группе для каждого предмета.
    Сохраняет students_full_report.json.
    """
    print("\n--- Задание 4: Объединение данных ---")
    try:
        # Читаем студентов
        with open("students.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            students = []
            for row in reader:
                students.append({
                    "student_id": int(row["student_id"]),
                    "name": row["name"],
                    "group": row["group"]
                })
        # Читаем оценки
        with open("grades.json", "r", encoding="utf-8") as f:
            grades = json.load(f)
        # Группируем оценки по student_id
        grades_by_student = defaultdict(list)
        for g in grades:
            sid = g["student_id"]
            grades_by_student[sid].append({
                "subject": g["subject"],
                "grade": g["grade"]
            })
        # Формируем отчёт по студентам
        report = []
        for student in students:
            sid = student["student_id"]
            student_grades = grades_by_student.get(sid, [])
            if student_grades:
                avg = sum(g["grade"] for g in student_grades) / len(student_grades)
            else:
                avg = 0
            if avg >= 4.5:
                status = "отличник"
            elif avg >= 3.5:
                status = "хорошист"
            else:
                status = "троечник"
            report.append({
                "student_id": sid,
                "name": student["name"],
                "group": student["group"],
                "grades": student_grades,
                "average": round(avg, 2),
                "status": status
            })
        # Вычисляем средний балл по группе для каждого предмета
        # Сначала собираем все оценки по группам и предметам
        group_subject_grades = defaultdict(lambda: defaultdict(list))
        for student in students:
            sid = student["student_id"]
            group = student["group"]
            for g in grades_by_student.get(sid, []):
                subj = g["subject"]
                grade = g["grade"]
                group_subject_grades[group][subj].append(grade)
        group_averages = {}
        for group, subjects in group_subject_grades.items():
            group_averages[group] = {}
            for subj, gradelist in subjects.items():
                group_averages[group][subj] = round(sum(gradelist) / len(gradelist), 2)
        # Добавляем в отчёт (можно отдельным ключом, но по заданию не требуется)
        # Сохраняем
        with open("students_full_report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"✅ Сохранён students_full_report.json для {len(report)} студентов")
        # Выведем для примера средние по группам
        for group, subs in group_averages.items():
            print(f"   Группа {group}: {subs}")
    except Exception as e:
        print(f"❌ Ошибка в задании 4: {e}")

# ============================================================
# ЗАДАНИЕ 5: Исправление и очистка данных (5 баллов)
# ============================================================

def clean_phone(phone):
    """Приводит телефон к формату +7-XXX-XXX-XX-XX."""
    # Удаляем всё кроме цифр и знака +
    digits = re.sub(r"[^\d+]", "", phone)
    # Если начинается с 8, заменяем на +7
    if digits.startswith("8"):
        digits = "+7" + digits[1:]
    elif not digits.startswith("+"):
        digits = "+7" + digits
    # Оставляем только цифры (без +)
    nums = re.sub(r"\D", "", digits)
    if len(nums) == 11 and nums.startswith("7"):
        # Форматируем
        formatted = f"+7-{nums[1:4]}-{nums[4:7]}-{nums[7:9]}-{nums[9:11]}"
        return formatted
    else:
        return None

def clean_email(email):
    """Проверяет корректность email: должен содержать @ и точку после @."""
    email = email.strip()
    # Простая проверка
    if "@" in email and "." in email.split("@")[-1]:
        return email
    return None

def clean_age(age_str):
    """Извлекает число из строки возраста."""
    match = re.search(r"\d+", age_str)
    if match:
        return int(match.group())
    return None

def task5_clean():
    """
    Читает dirty_data.csv, очищает поля:
    - Имя: удаляет лишние пробелы, делает заглавной первую букву каждого слова
    - Телефон: формат +7-XXX-XXX-XX-XX
    - Email: проверка
    - Возраст: только число
    Удаляет строки с неудачной очисткой.
    Добавляет поле Валидный.
    Сохраняет clean_data.csv и clean_data.json.
    """
    print("\n--- Задание 5: Очистка данных ---")
    try:
        with open("dirty_data.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        cleaned = []
        for row in rows:
            # Очистка имени
            name = row["Имя"].strip()
            name = " ".join(word.capitalize() for word in name.split())
            # Очистка телефона
            phone = clean_phone(row["Телефон"])
            # Очистка email
            email = clean_email(row["Email"])
            # Очистка возраста
            age = clean_age(row["Возраст"])
            # Валидность: все поля не None
            valid = (name and phone and email and age is not None)
            if valid:
                cleaned.append({
                    "Имя": name,
                    "Телефон": phone,
                    "Email": email,
                    "Возраст": age,
                    "Валидный": valid
                })
            else:
                # Добавляем даже невалидные, но с флагом False (по заданию: удалить строки где не удалось очистить)
                # По условию "удалите строки, где не удалось очистить данные" — не добавляем.
                pass
        # Сохраняем CSV
        if cleaned:
            with open("clean_data.csv", "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["Имя", "Телефон", "Email", "Возраст", "Валидный"])
                writer.writeheader()
                writer.writerows(cleaned)
            # Сохраняем JSON
            with open("clean_data.json", "w", encoding="utf-8") as f:
                json.dump(cleaned, f, ensure_ascii=False, indent=2)
            print(f"✅ Очищено {len(cleaned)} записей (из {len(rows)})")
        else:
            print("⚠ Нет валидных записей после очистки")
    except Exception as e:
        print(f"❌ Ошибка в задании 5: {e}")

# ============================================================
# ЗАДАНИЕ 6: Генератор отчетов (5 баллов)
# ============================================================

def task6_report():
    """
    На основе данных из задания 3 (продажи) генерирует текстовый отчёт.
    """
    print("\n--- Задание 6: Генератор отчётов ---")
    try:
        # Используем данные из sales.csv, чтобы не зависеть от предыдущих
        with open("sales.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            sales = []
            for row in reader:
                qty = int(row["Количество"])
                price = int(row["Цена"])
                revenue = qty * price
                sales.append({
                    "Товар": row["Товар"],
                    "Выручка": revenue
                })
        # Группируем по товарам
        product_revenue = defaultdict(int)
        for s in sales:
            product_revenue[s["Товар"]] += s["Выручка"]
        # Сортируем по выручке
        sorted_products = sorted(product_revenue.items(), key=lambda x: x[1], reverse=True)
        # Топ-5
        top5 = sorted_products[:5]
        # Группировка по категориям (для примера: Ноутбук -> Техника, Мышь/Клавиатура -> Периферия)
        category_revenue = defaultdict(int)
        for prod, rev in product_revenue.items():
            if prod == "Ноутбук":
                category_revenue["Техника"] += rev
            else:
                category_revenue["Периферия"] += rev
        total_rev = sum(product_revenue.values())
        # Формирование отчёта
        report_lines = []
        report_lines.append("=" * 40)
        report_lines.append("ОТЧЕТ ПО ДАННЫМ")
        report_lines.append("=" * 40)
        report_lines.append(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"Количество записей (продаж): {len(sales)}")
        report_lines.append("ТОП-5 ПО ВЫРУЧКЕ:")
        for i, (prod, rev) in enumerate(top5, 1):
            report_lines.append(f"{i}. {prod} - {rev} руб.")
        report_lines.append("ГРУППИРОВКА ПО КАТЕГОРИЯМ:")
        for cat, rev in category_revenue.items():
            percent = (rev / total_rev) * 100 if total_rev else 0
            report_lines.append(f"{cat}: {rev} руб. ({percent:.0f}%)")
        report_lines.append("=" * 40)
        report_text = "\n".join(report_lines)
        # Сохраняем отчёт в файл
        with open("report.txt", "w", encoding="utf-8") as f:
            f.write(report_text)
        print("✅ Отчёт сгенерирован в report.txt")
        print(report_text)
    except Exception as e:
        print(f"❌ Ошибка в задании 6: {e}")

# ============================================================
# ЗАДАНИЕ 7: Валидатор перед конвертацией (4 балла)
# ============================================================

def validate_csv_before_convert(filename):
    """
    Проверяет CSV файл на ошибки:
    - существование файла
    - наличие заголовков
    - нет пустых строк
    - все строки имеют одинаковое количество полей
    - нет пропущенных значений (пустые поля)
    Возвращает словарь с результатами.
    """
    print(f"\n--- Задание 7: Валидатор для {filename} ---")
    result = {
        "file_exists": False,
        "headers_found": False,
        "headers": [],
        "empty_lines": 0,
        "inconsistent_lines": [],  # номера строк с неверным числом полей
        "missing_values": 0,       # количество ячеек с пустыми значениями
        "can_convert": False
    }
    import os
    if not os.path.exists(filename):
        print(f"❌ Файл {filename} не найден")
        return result
    result["file_exists"] = True
    try:
        with open(filename, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = None
            expected_fields = None
            for line_num, row in enumerate(reader, start=1):
                # Пропускаем пустые строки
                if not any(row):
                    result["empty_lines"] += 1
                    continue
                if line_num == 1:
                    headers = row
                    expected_fields = len(headers)
                    if headers and all(h.strip() for h in headers):
                        result["headers_found"] = True
                        result["headers"] = headers
                    else:
                        result["headers_found"] = False
                else:
                    # Проверка количества полей
                    if len(row) != expected_fields:
                        result["inconsistent_lines"].append(line_num)
                    # Проверка пропущенных значений
                    for cell in row:
                        if cell == "" or cell.strip() == "":
                            result["missing_values"] += 1
        # Решение о конвертации
        if (result["file_exists"] and result["headers_found"] and
            result["empty_lines"] == 0 and len(result["inconsistent_lines"]) == 0):
            result["can_convert"] = True
        else:
            result["can_convert"] = False
        # Вывод результатов
        print(f"✅ Файл найден" if result["file_exists"] else "❌ Файл не найден")
        print(f"✅ Заголовки найдены: {len(result['headers'])} полей" if result["headers_found"] else "❌ Заголовки отсутствуют")
        if result["empty_lines"] > 0:
            print(f"⚠️ Пустых строк: {result['empty_lines']}")
        if result["inconsistent_lines"]:
            print(f"❌ Ошибка в строках {result['inconsistent_lines']}: не хватает полей")
        if result["missing_values"] > 0:
            print(f"⚠️ Пропущенных значений (пустых ячеек): {result['missing_values']}")
        print(f"Можно конвертировать? {'Да' if result['can_convert'] else 'Нет'}")
        return result
    except Exception as e:
        print(f"❌ Ошибка при проверке: {e}")
        return result

# ============================================================
# ОСНОВНОЙ БЛОК ЗАПУСКА
# ============================================================

if __name__ == "__main__":
    # Создаём исходные файлы
    create_initial_files()
    # Запускаем все задания
    task1_books()
    task2_employees()
    task3_sales()
    task4_merge()
    task5_clean()
    task6_report()
    # Для задания 7 проверим несколько файлов
    validate_csv_before_convert("students.csv")
    validate_csv_before_convert("dirty_data.csv")
    print("\n✅ Все задания выполнены.")