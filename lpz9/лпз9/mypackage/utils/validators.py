"""
Модуль validators - функции для валидации данных.
"""

import re

def validate_email(email):
    """
    Проверяет корректность email адреса.

    Returns:
        tuple: (is_valid, error_message)
    """
    if not email:
        return False, "Email не может быть пустым"
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, "Email корректен"
    else:
        return False, "Некорректный формат email"

def validate_age(age):
    """Проверяет корректность возраста."""
    if not isinstance(age, (int, float)):
        return False, "Возраст должен быть числом"
    if age < 16:
        return False, "Студент должен быть старше 16 лет"
    if age > 100:
        return False, "Некорректный возраст"
    return True, "Возраст корректен"

def validate_grade(grade):
    """Проверяет корректность оценки."""
    if not isinstance(grade, (int, float)):
        return False, "Оценка должна быть числом"
    if grade < 2 or grade > 5:
        return False, "Оценка должна быть от 2 до 5"
    return True, "Оценка корректна"

def validate_name(name):
    """Проверяет корректность имени/фамилии."""
    if not name or not isinstance(name, str):
        return False, "Имя не может быть пустым"
    if len(name) < 2:
        return False, "Имя должно содержать минимум 2 символа"
    if not name.replace('-', '').replace(' ', '').isalpha():
        return False, "Имя должно содержать только буквы"
    return True, "Имя корректно"