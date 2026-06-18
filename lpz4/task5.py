"""
Задание 5: Сложение через разделитель
"""
dct = {'a': 7, 'b': 6, 'c': 5}
result = '/'.join(str(v) for v in sorted(dct.values()))
print(result)