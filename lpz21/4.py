def crossing_time(times):
    times.sort()
    total = 0
    while len(times) > 3:
        a, b = times[0], times[1]
        y, z = times[-2], times[-1]
        # два способа: 1) a+b туда, a назад, y+z туда, b назад
        way1 = b + a + z + b
        # 2) a+z туда, a назад, a+y туда, a назад
        way2 = z + a + y + a
        if way1 < way2:
            total += way1
        else:
            total += way2
        times.pop()
        times.pop()
    if len(times) == 3:
        total += times[0] + times[1] + times[2]
    elif len(times) == 2:
        total += times[1]
    else:
        total += times[0]
    return total

people = [1, 2, 5, 10]
print("Минимальное время:", crossing_time(people))