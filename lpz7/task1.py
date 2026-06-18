"""
Задание 1: match-case
"""
num = 2  # номер поры года: 1-весна, 2-лето, 3-осень, 4-зима

match num:
    case 1:
        print("Весна")
    case 2:
        print("Лето")
    case 3:
        print("Осень")
    case 4:
        print("Зима")