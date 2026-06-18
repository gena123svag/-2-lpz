"""
Задание 4: Сложение как строки
"""
dct = {'x': 1, 'y': 2, 'z': 3}
result = ''.join(str(v) for v in dct.values())
print(result)