"""
Задание 3: Проверка email на '@'
"""
email = input("Введите email: ")
if '@' not in email:
    email = input("Некорректный email. Введите снова: ")
print(f"Ваш email: {email}")