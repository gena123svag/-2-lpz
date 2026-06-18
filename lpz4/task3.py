"""
Задание 3: Преобразование значений в строки
"""
dct = {1: '4', 2: '5', 3: '6'}
str_dict = {k: str(v) for k, v in dct.items()}
print(str_dict)