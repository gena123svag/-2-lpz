import re

# 1.1 Email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, "✅ Email корректный"
    return False, "❌ Неправильный email! Пример: name@mail.ru"

# 1.2 Телефон
def validate_phone(phone):
    phone = phone.strip()
    patterns = [
        r'^\+7-\d{3}-\d{3}-\d{2}-\d{2}$',
        r'^\+7 \d{3} \d{3} \d{2} \d{2}$',
        r'^\+7\d{10}$',
        r'^8-\d{3}-\d{3}-\d{4}$',
        r'^8 \d{3} \d{3} \d{4}$',
        r'^8\d{10}$'
    ]
    for pattern in patterns:
        if re.match(pattern, phone):
            clean = re.sub(r'\D', '', phone)
            if clean.startswith('8'):
                clean = '+7' + clean[1:]
            elif clean.startswith('7'):
                clean = '+' + clean
            return True, "✅ Телефон корректный", clean
    return False, "❌ Неправильный телефон! Пример: +7-999-123-45-67", None

# 1.3 ИНН
def validate_inn(inn):
    inn = inn.strip()
    if not inn.isdigit():
        return False, "❌ ИНН должен содержать только цифры!"
    if len(inn) == 10:
        return True, "✅ ИНН организации (10 цифр)"
    elif len(inn) == 12:
        return True, "✅ ИНН физ. лица (12 цифр)"
    return False, "❌ ИНН должен содержать 10 или 12 цифр!"

# Самостоятельное задание 1: Проверка паспорта (формат 45 03 123456)
def validate_passport(passport):
    pattern = r'^\d{2} \d{2} \d{6}$'
    if re.match(pattern, passport.strip()):
        return True, "✅ Паспорт корректен"
    return False, "❌ Неправильный формат паспорта! Пример: 45 03 123456"

# Тестирование валидации
if __name__ == "__main__":
    print("=== Тест валидации email ===")
    for email in ["user@mail.ru", "test@gmail.com", "invalid-email", "user@domain"]:
        valid, msg = validate_email(email)
        print(f"{email}: {msg}")

    print("\n=== Тест валидации телефона ===")
    for phone in ["+7-999-123-45-67", "+7 999 123 45 67", "+79991234567", "8-999-123-4567", "12345"]:
        valid, msg, clean = validate_phone(phone)
        print(f"{phone}: {msg}")
        if valid:
            print(f"   Очищенный: {clean}")

    print("\n=== Тест валидации ИНН ===")
    for inn in ["7712345678", "123456789012", "12345", "12a34567890"]:
        valid, msg = validate_inn(inn)
        print(f"{inn}: {msg}")

    print("\n=== Тест валидации паспорта ===")
    for passport in ["45 03 123456", "45 03 12345", "1234 567890"]:
        valid, msg = validate_passport(passport)
        print(f"{passport}: {msg}")