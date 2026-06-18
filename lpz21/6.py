def step(robots):
    n = len(robots)
    new = robots[:]  # копия
    for i in range(n):
        if robots[i] % 2 == 0:  # чётный, меняем с правым
            if i + 1 < n:
                new[i], new[i+1] = new[i+1], new[i]
        else:  # нечётный, меняем с левым
            if i - 1 >= 0:
                new[i], new[i-1] = new[i-1], new[i]
    return new

robots = [1, 2, 3, 4, 5, 6, 7]
print("Начало:", robots)
after1 = step(robots)
print("Через 1 сек:", after1)
after2 = step(after1)
print("Через 2 сек:", after2)