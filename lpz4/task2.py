"""
Задание 2: Сложение значений словарей
"""
dct1 = {'1': 12, '2': 24, '3': 36}
dct2 = {'a': '3', 'b': '6', 'c': '9'}
sum1 = sum(dct1.values())
sum2 = sum(int(v) for v in dct2.values())
result = sum1 - sum2
print(f"Сумма dct1: {sum1}")
print(f"Сумма dct2: {sum2}")
print(f"Результат: {result}")