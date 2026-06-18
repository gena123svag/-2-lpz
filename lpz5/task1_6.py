"""
Задание 6: Последняя буква слова
"""
word = input("Введите слово: ")
if word.endswith('ь') or word.endswith('ъ'):
    print(word[-2])
else:
    print(word[-1])