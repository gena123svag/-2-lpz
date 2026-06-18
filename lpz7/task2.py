"""
Задание 2: Вложенный if
"""
num = 45

if 10 <= num <= 99:
    sum_digits = (num // 10) + (num % 10)
    if sum_digits <= 9:
        print("Сумма цифр однозначна")
    else:
        print("Сумма цифр двухзначная")