"""
Задание 1: Сумма квадратов элементов словаря
"""
dct = {'x': '1', 'y': '2', 'z': '3'}
total = sum(int(v) ** 2 for v in dct.values())
print(total)