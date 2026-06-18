"""
Задание 2: Замена символа 'a' на '!'
"""
txt = input("Введите строку: ")
if 'a' in txt:
    txt = txt.replace('a', '!')
print(txt)