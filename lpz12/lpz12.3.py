import re

# ---------- Валидация ----------
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return (True, "✅ Email корректный") if re.match(pattern, email) else (False, "❌ Неправильный email!")

def validate_phone(phone):
    phone = phone.strip()
    patterns = [
        r'^\+7-\d{3}-\d{3}-\d{2}-\d{2}$', r'^\+7 \d{3} \d{3} \d{2} \d{2}$',
        r'^\+7\d{10}$', r'^8-\d{3}-\d{3}-\d{4}$', r'^8 \d{3} \d{3} \d{4}$', r'^8\d{10}$'
    ]
    for p in patterns:
        if re.match(p, phone):
            clean = re.sub(r'\D', '', phone)
            if clean.startswith('8'):
                clean = '+7' + clean[1:]
            elif clean.startswith('7'):
                clean = '+' + clean
            return True, "✅ Телефон корректен", clean
    return False, "❌ Неправильный телефон! Пример: +7-999-123-45-67", None

def validate_inn(inn):
    inn = inn.strip()
    if not inn.isdigit():
        return False, "❌ Только цифры!"
    if len(inn) == 10:
        return True, "✅ ИНН организации (10 цифр)"
    if len(inn) == 12:
        return True, "✅ ИНН физ. лица (12 цифр)"
    return False, "❌ Нужно 10 или 12 цифр!"

def validate_passport(passport):
    if re.match(r'^\d{2} \d{2} \d{6}$', passport.strip()):
        return True, "✅ Паспорт корректен"
    return False, "❌ Формат: 45 03 123456"

# ---------- Поиск ----------
def find_emails(text):
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

def find_phones(text):
    return re.findall(r'\+7[- ]?\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}|8[- ]?\d{3}[- ]?\d{3}[- ]?\d{4}', text)

def find_dates(text):
    return re.findall(r'\d{2}[./]\d{2}[./]\d{4}', text)

def find_prices(text):
    return re.findall(r'\d+(?:[.,]\d+)?\s?(?:руб|₽|\$|€)', text)

def find_urls(text):
    return re.findall(r'https?://[a-zA-Z0-9./?=_-]+|www\.[a-zA-Z0-9./?=_-]+', text)

def find_ips(text):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.findall(ip_pattern, text)

def find_hashtags(text):
    return re.findall(r'#[a-zA-Zа-яА-Я0-9_]+', text, re.IGNORECASE)

# ---------- Главное меню ----------
def main():
    while True:
        print("\n" + "="*50)
        print("ПРОГРАММА ВАЛИДАЦИИ И ПОИСКА")
        print("1. Проверить email")
        print("2. Проверить телефон")
        print("3. Проверить ИНН")
        print("4. Проверить паспорт")
        print("5. Поиск данных в тексте")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "0":
            print("До свидания!")
            break
        elif choice == "1":
            email = input("Введите email: ")
            valid, msg = validate_email(email)
            print(msg)
        elif choice == "2":
            phone = input("Введите телефон: ")
            valid, msg, clean = validate_phone(phone)
            print(msg)
            if valid:
                print(f"Очищенный: {clean}")
        elif choice == "3":
            inn = input("Введите ИНН: ")
            valid, msg = validate_inn(inn)
            print(msg)
        elif choice == "4":
            passport = input("Введите паспорт (формат 45 03 123456): ")
            valid, msg = validate_passport(passport)
            print(msg)
        elif choice == "5":
            print("Введите текст (пустая строка + Enter для завершения):")
            lines = []
            while True:
                line = input()
                if line == "" and lines:
                    break
                lines.append(line)
            text = "\n".join(lines)

            print("\n" + "="*50)
            print("РЕЗУЛЬТАТЫ ПОИСКА:")
            results = {
                "Email": find_emails(text),
                "Телефоны": find_phones(text),
                "Даты": find_dates(text),
                "Цены": find_prices(text),
                "Ссылки": find_urls(text),
                "IP-адреса": find_ips(text),
                "Хэштеги": find_hashtags(text)
            }
            found = False
            for name, items in results.items():
                if items:
                    print(f"{name}: {items}")
                    found = True
            if not found:
                print("Ничего не найдено.")
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()