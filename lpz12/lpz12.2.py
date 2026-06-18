import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def find_phones(text):
    pattern = r'\+7[- ]?\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}|8[- ]?\d{3}[- ]?\d{3}[- ]?\d{4}'
    return re.findall(pattern, text)

def find_dates(text):
    pattern = r'\d{2}[./]\d{2}[./]\d{4}'
    return re.findall(pattern, text)

def find_prices(text):
    pattern = r'\d+(?:[.,]\d+)?\s?(?:руб|₽|\$|€)'
    return re.findall(pattern, text)

def find_urls(text):
    pattern = r'https?://[a-zA-Z0-9./?=_-]+|www\.[a-zA-Z0-9./?=_-]+'
    return re.findall(pattern, text)

# Самостоятельное задание 2: поиск IP-адресов
def find_ips(text):
    # Каждое число от 0 до 255, не более трёх цифр
    pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.findall(pattern, text)

# Самостоятельное задание 3: поиск хэштегов
def find_hashtags(text):
    # #слово (буквы, цифры, подчёркивания, кириллица)
    pattern = r'#[a-zA-Zа-яА-Я0-9_]+'
    return re.findall(pattern, text, re.IGNORECASE)

# Тестирование поиска
if __name__ == "__main__":
    sample_text = """
    Контакты: ivan@mail.ru и petr@gmail.com.
    Звоните: +7-999-123-45-67 или 8 800 555 35 35.
    Даты: 15.05.2025 и 20/12/2026.
    Цены: 50000 руб, 1500₽, $80.
    Ссылки: https://python.org и www.google.com.
    IP-адреса: 192.168.1.1 и 255.255.255.0, а также 999.999.999.999 (неправильный).
    Хэштеги: #python #программирование #regex123 #ИТ.
    """

    print("=== Поиск email ===", find_emails(sample_text))
    print("=== Поиск телефонов ===", find_phones(sample_text))
    print("=== Поиск дат ===", find_dates(sample_text))
    print("=== Поиск цен ===", find_prices(sample_text))
    print("=== Поиск ссылок ===", find_urls(sample_text))
    print("=== Поиск IP-адресов ===", find_ips(sample_text))
    print("=== Поиск хэштегов ===", find_hashtags(sample_text))