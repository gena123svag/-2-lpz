"""
Задание 1: Перебор словаря
"""
tst = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd'
}

result = []
for i, key in enumerate(tst):
    result.append(i)
    result.append(tst[key])

print(result)