"""
Задание 5: Множество из 10 букв алфавита
"""
letters = set()
for i in range(10):
    letters.add(chr(ord('a') + i))
print(letters)