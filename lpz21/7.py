def find_codes():
    codes = []
    for a in range(10):
        for b in range(10):
            if 2*a + b == 15:
                codes.append(f"{a}{b}{a}")
    return codes

print("Возможные коды:", find_codes())
print("Количество вариантов без подсказок: 1000")
print("С учётом палиндрома и суммы 15:", len(find_codes()))