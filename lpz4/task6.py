"""
Задание 6: Форматирование даты
"""
dct = {'y': 2025, 'm': 12, 'd': 31}
result = f"{dct['y']}-{dct['m']:02d}-{dct['d']:02d}"
print(result)