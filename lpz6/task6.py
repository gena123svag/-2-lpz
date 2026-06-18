"""
Задание 6: Тернарный оператор
"""
tst = 'abcdef'
result = 'string is too short' if len(tst) > 20 else 'string is too short'
print('string is too long' if len(tst) > 20 else 'string is too short')