containers = [12, 47, 35, 78, 97, 23, 67, 44, 57, 89]
danger = [num for num in containers if num % 10 == 7]
print("Опасные контейнеры:", danger)