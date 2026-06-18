import csv
import json

# ============================================================
# ЧАСТЬ 1: Создание исходных файлов
# ============================================================

def create_students_csv():
    """Создаёт файл students.csv с данными."""
    data = [
        ["Имя", "Фамилия", "Группа", "Возраст", "Средний_балл"],
        ["Иван", "Петров", "ПИН-231", "19", "4.5"],
        ["Анна", "Сидорова", "ПИН-231", "20", "4.8"],
        ["Петр", "Иванов", "ПИН-232", "18", "3.9"],
        ["Мария", "Кузнецова", "ПИН-232", "19", "4.9"],
        ["Алексей", "Смирнов", "ПИН-231", "20", "4.2"],
        ["Елена", "Попова", "ПИН-233", "19", "5.0"],
        ["Дмитрий", "Васильев", "ПИН-233", "21", "3.7"]
    ]
    with open("students.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print("✅ Файл students.csv создан")

def create_products_json():
    """Создаёт файл products.json с данными."""
    data = [
        {"id": 1, "name": "Ноутбук", "price": 50000, "quantity": 10},
        {"id": 2, "name": "Мышь", "price": 1500, "quantity": 50},
        {"id": 3, "name": "Клавиатура", "price": 3000, "quantity": 25}
    ]
    with open("products.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ Файл products.json создан")

# ============================================================
# ЧАСТЬ 2: Конвертеры CSV → JSON
# ============================================================

def csv_to_json(csv_filename, json_filename):
    """Простой конвертер CSV → JSON."""
    data = []
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Преобразование чисел
                for key in row:
                    if row[key].replace('.', '').isdigit():
                        if '.' in row[key]:
                            row[key] = float(row[key])
                        else:
                            row[key] = int(row[key])
                data.append(row)
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"✅ Успешно преобразовано: {csv_filename} → {json_filename}")
        print(f"   Записей: {len(data)}")
        return True
    except FileNotFoundError:
        print(f"❌ Ошибка: файл {csv_filename} не найден")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def students_csv_to_json(csv_filename, json_filename):
    """Расширенный конвертер для студентов (добавляет full_name и status)."""
    students = []
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                avg = float(row['Средний_балл'])
                student = {
                    "full_name": f"{row['Имя']} {row['Фамилия']}",
                    "group": row['Группа'],
                    "age": int(row['Возраст']),
                    "average_score": avg,
                    "status": "отличник" if avg >= 4.5 else "хорошист" if avg >= 3.5 else "нужно учиться"
                }
                students.append(student)
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(students, json_file, ensure_ascii=False, indent=4)
        print(f"✅ Конвертация студентов завершена! Результат: {json_filename}")
        for s in students:
            print(f"   {s['full_name']}: {s['status']}")
        return True
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

# ============================================================
# ЧАСТЬ 3: Конвертеры JSON → CSV
# ============================================================

def json_to_csv(json_filename, csv_filename):
    """Простой конвертер JSON → CSV."""
    try:
        with open(json_filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        if not data:
            print("❌ JSON файл пуст")
            return False
        headers = list(data[0].keys())
        with open(csv_filename, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Успешно преобразовано: {json_filename} → {csv_filename}")
        print(f"   Записей: {len(data)}")
        return True
    except FileNotFoundError:
        print(f"❌ Ошибка: файл {json_filename} не найден")
        return False
    except json.JSONDecodeError:
        print(f"❌ Ошибка: файл {json_filename} содержит некорректный JSON")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def products_json_to_csv(json_filename, csv_filename):
    """Расширенный конвертер для товаров (добавляет общую стоимость и категорию)."""
    try:
        with open(json_filename, 'r', encoding='utf-8') as json_file:
            products = json.load(json_file)
        enhanced_products = []
        for product in products:
            price = product['price']
            quantity = product['quantity']
            enhanced = {
                "ID": product['id'],
                "Название": product['name'],
                "Цена": price,
                "Количество": quantity,
                "Общая_стоимость": price * quantity,
                "Категория": "Электроника" if price > 10000 else "Аксессуары"
            }
            enhanced_products.append(enhanced)
        headers = ["ID", "Название", "Цена", "Количество", "Общая_стоимость", "Категория"]
        with open(csv_filename, 'w', encoding='utf-8', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(enhanced_products)
        print(f"✅ Конвертация товаров завершена! Результат: {csv_filename}")
        for p in enhanced_products:
            print(f"   {p['Название']}: {p['Общая_стоимость']} руб. ({p['Категория']})")
        return True
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

# ============================================================
# ЧАСТЬ 4: Универсальный конвертер (программа с меню)
# ============================================================

def read_csv_as_dicts(filename):
    """Читает CSV и возвращает список словарей."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        print(f"Ошибка чтения CSV: {e}")
        return None

def read_json_as_dicts(filename):
    """Читает JSON и возвращает список словарей."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                return [data]
            else:
                return None
    except Exception as e:
        print(f"Ошибка чтения JSON: {e}")
        return None

def save_as_csv(data, filename):
    """Сохраняет список словарей в CSV."""
    if not data:
        print("Нет данных для сохранения")
        return False
    try:
        headers = list(data[0].keys())
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Сохранено в {filename} ({len(data)} записей)")
        return True
    except Exception as e:
        print(f"Ошибка сохранения CSV: {e}")
        return False

def save_as_json(data, filename):
    """Сохраняет список словарей в JSON."""
    if not data:
        print("Нет данных для сохранения")
        return False
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✅ Сохранено в {filename} ({len(data)} записей)")
        return True
    except Exception as e:
        print(f"Ошибка сохранения JSON: {e}")
        return False

def convert_numbers(data):
    """Преобразует строки в числа, где это возможно."""
    for row in data:
        for key, value in row.items():
            if isinstance(value, str):
                if value.replace('.', '').replace('-', '').isdigit():
                    if '.' in value:
                        row[key] = float(value)
                    else:
                        row[key] = int(value)
    return data

def show_data_preview(data, title="Данные"):
    """Показывает предпросмотр данных (первые 5 записей)."""
    if not data:
        print("Нет данных")
        return
    print(f"\n📊 {title} (всего: {len(data)} записей)")
    print("-" * 50)
    headers = list(data[0].keys())
    print("Поля:", ", ".join(headers))
    print("\nПервые 5 записей:")
    for i, row in enumerate(data[:5], 1):
        print(f"  {i}. {row}")
    if len(data) > 5:
        print(f"  ... и еще {len(data) - 5} записей")

def main():
    """Главное меню универсального конвертера."""
    data = None
    current_file = None
    while True:
        print("\n" + "=" * 50)
        print("🔄 КОНВЕРТЕР ДАННЫХ CSV ↔ JSON")
        print("=" * 50)
        if current_file:
            print(f"📁 Текущие данные: {current_file} ({len(data) if data else 0} записей)")
        print("-" * 40)
        print("1. Загрузить CSV файл")
        print("2. Загрузить JSON файл")
        print("3. Показать данные")
        print("4. Преобразовать типы (строки → числа)")
        print("5. Сохранить как CSV")
        print("6. Сохранить как JSON")
        print("0. Выход")
        choice = input("\nВыберите действие: ").strip()
        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            filename = input("Введите имя CSV файла: ").strip()
            data = read_csv_as_dicts(filename)
            if data:
                current_file = filename
                convert_numbers(data)
                show_data_preview(data, f"CSV: {filename}")
        elif choice == "2":
            filename = input("Введите имя JSON файла: ").strip()
            data = read_json_as_dicts(filename)
            if data:
                current_file = filename
                convert_numbers(data)
                show_data_preview(data, f"JSON: {filename}")
        elif choice == "3":
            if data:
                show_data_preview(data)
            else:
                print("Нет загруженных данных")
        elif choice == "4":
            if data:
                data = convert_numbers(data)
                print("✅ Типы данных преобразованы")
                show_data_preview(data)
            else:
                print("Нет загруженных данных")
        elif choice == "5":
            if data:
                filename = input("Введите имя CSV файла для сохранения: ").strip()
                save_as_csv(data, filename)
            else:
                print("Нет данных для сохранения")
        elif choice == "6":
            if data:
                filename = input("Введите имя JSON файла для сохранения: ").strip()
                save_as_json(data, filename)
            else:
                print("Нет данных для сохранения")
        else:
            print("Неверный выбор!")

# ============================================================
# ЗАПУСК
# ============================================================

if __name__ == "__main__":
    print("=== Лабораторная работа №13: Конвертер данных ===\n")

    # Часть 1: создание исходных файлов
    create_students_csv()
    create_products_json()

    # Часть 2: конвертеры CSV → JSON
    print("\n--- Часть 2: Конвертеры CSV → JSON ---")
    csv_to_json("students.csv", "students.json")
    students_csv_to_json("students.csv", "students_enhanced.json")

    # Часть 3: конвертеры JSON → CSV
    print("\n--- Часть 3: Конвертеры JSON → CSV ---")
    json_to_csv("products.json", "products.csv")
    products_json_to_csv("products.json", "products_enhanced.csv")

    # Часть 4: универсальный конвертер с меню
    print("\n--- Часть 4: Универсальный конвертер ---")
    main()