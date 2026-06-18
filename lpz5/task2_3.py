"""
Задание 3: Сумма первой и последней цифры
"""
num = abs(int(input("Введите число: ")))
first = int(str(num)[0])
last = num % 10
print(first + last)